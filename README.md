# GitHub Users Analysis

- This project uses data from the GitHub API to analyze users and repositories in Zurich, focusing on trends and interesting metrics.
- The most surprising insight we found is that developers who create more repositories tend to gain more followers, suggesting that contributing more makes a developer more visible.
- Developers should enable features like "projects" and "wikis" on their repositories to encourage better community engagement.

## Project Overview
This project analyzes GitHub users in Zurich who have more than 50 followers. We extracted their profile data and information about their public repositories to understand trends in the open source community. The analysis aims to answer several questions, such as which companies are most popular among these developers, which languages they use, and what makes developers more successful on GitHub.

## Files in Repository
- `users.csv`: Contains information about GitHub users in Zurich with more than 50 followers, including their name, company, location, email, and more.
- `repositories.csv`: Includes data about these users' public repositories, such as the name, programming language, star count, and features like projects or wikis.
- `README.md`: The document you are reading right now, which explains the purpose, methodology, and findings of this project.

## Data Collection Process
The data for this project was collected using the GitHub API. We used Python to make requests to the API, processed the responses to extract useful information, and stored this information in CSV files for easier analysis. During this process, we cleaned up company names, removed any special characters or unnecessary symbols, and standardized formats.

## Key Insights
1. **Popularity and Repository Count**: Developers who create more public repositories tend to have more followers. The regression analysis showed that each additional repository adds, on average, around 1.466 followers.

2. **Company Affiliation**: A majority of developers in Zurich work for Google. It seems like Google has a large pool of talent in Zurich, and many of them are active contributors on GitHub.

3. **Programming Language Trends**: Python is the most popular programming language among these users, followed by JavaScript. Interestingly, for developers who joined after 2020, JavaScript has gained significant traction.

4. **Open Source Engagement**: Many developers choose not to use any license for their projects. Among those who do, the MIT License is the most common. This suggests that developers are open to sharing their work freely with minimal restrictions.

5. **Features for Collaboration**: The correlation between enabling "projects" and "wikis" on a repository is moderately positive. Enabling these features can be a good way to encourage more community involvement and collaboration.

6. **Surname Trends**: The most common surnames among the developers in Zurich are "Li" and "Wang," indicating a significant number of contributors with Chinese heritage.

7. **Email Sharing Behavior**: Developers who are hireable are more likely to share their email addresses compared to those who are not hireable. The difference in sharing is approximately 7.8%, showing that those looking for opportunities are more open to being contacted.

8. **Leader Strength**: By defining "leader strength" as followers divided by (1 + following), we found that the top users are those who have more followers compared to the people they follow. This metric highlights prominent figures in the GitHub community who contribute quality work.

## Recommendation for Developers
Based on the analysis, developers looking to grow their followers should focus on creating more public repositories and enabling collaboration features like "projects" and "wikis." Additionally, being active, approachable, and sharing contact information can significantly boost community engagement and lead to new opportunities.

