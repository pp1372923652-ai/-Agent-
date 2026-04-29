import os
from github import Github

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_repo(repo_name):
    g = Github(GITHUB_TOKEN)
    return g.get_repo(repo_name)

def create_pr(repo, branch_name, body):
    pr = repo.create_pull(
        title=f"Automated code review for {branch_name}",
        body=body,
        head=branch_name,
        base="main"
    )
    return pr.html_url
