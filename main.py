import pandas as pd
import requests
import csv
import re
import time

# Use your GitHub token
TOKEN = "Your Token"
headers = {'Authorization': f'token {TOKEN}'}

# GitHub search URL for users in Zurich with > 50 followers
search_url = "https://api.github.com/search/users?q=location:Zurich+followers:>50"

# Function to clean up company names
def clean_company_name(company):
    if company:
        company = company.strip()
        company = re.sub(r'^@', '', company)
        company = company.upper()
    return company or ''

def fetch_users_with_pagination(url, headers):
    all_users = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break

        # Get the users from the current page
        users = response.json().get('items', [])
        all_users.extend(users)

        # Check for the 'next' page link in the 'Link' header
        if 'Link' in response.headers:
            links = response.headers['Link']
            next_link = None
            for link in links.split(','):
                if 'rel="next"' in link:
                    next_link = link.split(';')[0].strip()[1:-1]
            url = next_link  # Update the URL to the next page
        else:
            url = None  # No more pages
    return all_users

# Fetch users with pagination
users = fetch_users_with_pagination(search_url, headers)

# Prepare CSV for users
with open('users.csv', mode='w', newline='') as users_file:
    users_writer = csv.writer(users_file)
    # Write headers for users.csv
    users_writer.writerow(['login', 'name', 'company', 'location', 'email', 'hireable', 'bio', 'public_repos', 'followers', 'following', 'created_at'])

    # Loop through each user
    for user in users:
        login = user['login']
        user_url = f"https://api.github.com/users/{login}"
        user_data = requests.get(user_url, headers=headers).json()

        # Clean and prepare user details
        name = user_data.get('name', '')
        company = clean_company_name(user_data.get('company', ''))
        location = user_data.get('location', '')
        email = user_data.get('email', '')
        hireable = user_data.get('hireable', False)
        bio = user_data.get('bio', '')
        public_repos = user_data.get('public_repos', 0)
        followers = user_data.get('followers', 0)
        following = user_data.get('following', 0)
        created_at = user_data.get('created_at', '')

        # Write user data to users.csv
        users_writer.writerow([login, name, company, location, email, hireable, bio, public_repos, followers, following, created_at])

# Load the users.csv file
users_df = pd.read_csv('users.csv')
users_logins = users_df['login'].tolist()

def fetch_repositories(login):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{login}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            repo_data = response.json()
            if not repo_data:
                break  # No more repositories on this page
            repos.extend(repo_data)
            page += 1
        else:
            print(f"Failed to fetch repos for {login}: {response.status_code}")
            if response.status_code == 403:  # Rate limiting
                reset_time = int(response.headers.get('X-RateLimit-Reset', time.time()))
                sleep_duration = reset_time - time.time() + 10  # Sleep until rate limit is reset
                print(f"Rate limited. Sleeping for {sleep_duration} seconds...")
                time.sleep(sleep_duration)
            else:
                break
    return repos

# Prepare the output CSV for repositories
with open('repositories.csv', mode='w', newline='') as repos_file:
    repos_writer = csv.writer(repos_file)
    # Write headers for the repositories.csv file
    repos_writer.writerow(['login', 'full_name', 'created_at', 'stargazers_count', 'watchers_count', 'language', 'has_projects', 'has_wiki', 'license_name'])

    # Loop through each user in the users.csv
    for idx, login in enumerate(users_logins):
        print(f"Fetching repositories for user: {login} ({idx + 1}/{len(users_logins)})")

        # Fetch repositories for the current user
        user_repos = fetch_repositories(login)

        # Write the repositories to the output CSV file
        for repo in user_repos:
            license_info = repo.get('license')
            license_name = license_info['name'] if license_info else 'No License'

            repos_writer.writerow([
                login,
                repo.get('full_name', ''),
                repo.get('created_at', ''),
                repo.get('stargazers_count', 0),
                repo.get('watchers_count', 0),
                repo.get('language', ''),
                repo.get('has_projects', False),
                repo.get('has_wiki', False),
                license_name
            ])

        # Display progress after each user
        users_left = len(users_logins) - (idx + 1)
        print(f"Progress: {users_left} users left")

print("Finished fetching repositories.")
