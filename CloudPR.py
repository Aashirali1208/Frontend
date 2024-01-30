import streamlit as st
import requests

def get_github_stats(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def generate_github_cv(username, github_stats):
    if github_stats is not None:
        cv = f"""
        # GitHub CV for {username}

        ## Profile
        - **Username:** {username}
        - **Name:** {github_stats.get('name', 'N/A')}
        - **Location:** {github_stats.get('location', 'N/A')}

        ## Stats
        - **Public Repositories:** {github_stats.get('public_repos', 0)}
        - **Followers:** {github_stats.get('followers', 0)}
        - **Following:** {github_stats.get('following', 0)}

        ## Skills
        - {", ".join(["Python", "JavaScript", "React", "Node.js", "Git"])}

        ## Recent Repositories
        """
        for repo in github_stats.get('repos_url', []):
            cv += f"- [{repo['name']}]({repo['html_url']})\n"
    else:
        cv = "Unable to fetch GitHub data. Please check your username."

    return cv

# Streamlit App
st.title("GitHub CV Generator")

# User input
username = st.text_input("GitHub Username:")

if st.button("Generate GitHub CV"):
    github_stats = get_github_stats(username)
    cv = generate_github_cv(username, github_stats)
    st.markdown(cv)
