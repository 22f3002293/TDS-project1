# GitHub Users Analysis

## An Explanation of How i Scraped the Data
- The data for this project was collected using the GitHub API, which gave us access to information about users and their repositories.
- We used Python scripts to get data from the API and processed it to extract user profiles, repository details, and activity.
- The information was saved in CSV files for easy analysis.
- We cleaned the data by standardizing company names—removing extra spaces, symbols like "@", and making everything uppercase for consistency.
- We focused on users in Zurich with over 50 followers to make sure the dataset was big enough for useful insights.

## The Most Interesting and Surprising Fact i Found After Analyzing the Data
1. **Popularity and Repository Count**: Developers who create more public repositories usually have more followers. Each additional repository adds, on average, around 1.5 followers.

2. **Company Affiliation**: Most developers in Zurich work for Google. It seems Google has many talented developers in Zurich who are active on GitHub.

3. **Programming Language Trends**: Python is the most popular language among these users, followed by JavaScript. For developers who joined after 2020, JavaScript has become more popular.

4. **Open Source Engagement**: Many developers don't use a license for their projects. Among those who do, the MIT License is the most common, showing that they are open to sharing their work with few restrictions.

5. **Features for Collaboration**: There is a positive link between using "projects" and "wikis" on repositories. Turning on these features can help get more people involved and make collaboration easier.

6. **Surname Trends**: The most common surnames among developers in Zurich are "Li" and "Wang," suggesting many contributors have Chinese heritage.

7. **Email Sharing Behavior**: Developers who are hireable are more likely to share their email addresses than those who aren't. The difference is around 7.8%, meaning hireable developers are more open to being contacted.

8. **Leader Strength**: We defined "leader strength" as followers divided by (1 + following). Top users are those with more followers than people they follow, showing they are key figures who provide valuable work.

## An Actionable Recommendation for Developers Based on my Analysis
- To grow their following, developers should be more active by creating and sharing public repositories. Contributing more projects shows skills and attracts attention from others.
- Turning on collaboration features like "projects" and "wikis" can boost engagement by making it easier for others to contribute and understand the work.
- Sharing contact details, like an email address, can make a developer more visible to collaborators or employers.
- Developers looking for new opportunities should mark themselves as "hireable" and share their contact information to increase their chances of being approached.
- Companies should encourage developers to be visible on GitHub to build their reputation and support a culture of sharing and learning.

