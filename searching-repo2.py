# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:57:13 2023

@author: monster
"""
from github import Github

# Github username
username = "Ckudat"
# pygithub object
g = Github(input("access token: "))
# get that user by username
user = g.get_user(username)
def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)
    # repository description
    print("Description:", repo.description)
    # the date of when the repo was created
    print("Date created:", repo.created_at)
    # the date of the last git push
    print("Date of last push:", repo.pushed_at)
    # home website (if available)
    print("Home Page:", repo.homepage)
    # programming language
    print("Language:", repo.language)
    # number of forks
    print("Number of forks:", repo.forks)
    # number of stars
    print("Number of stars:", repo.stargazers_count)
    print("-"*50)
    # repository content (files & directories)
    print("Contents:")
    for content in repo.get_contents(""):
        print(content)
    
# search by programming language
for i, repo in enumerate(g.search_repositories("language:python")):
    print_repo(repo)
    print("="*100)
    if i == 9:
        break