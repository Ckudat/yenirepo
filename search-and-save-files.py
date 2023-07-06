# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:52:21 2023

@author: monster
"""

import base64
import github
import sys
import os

# make a directory to save the Python files
if not os.path.exists("javascript-files"):
    os.mkdir("javascript-files")


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
    try:
        for content in repo.get_contents(""):
            # check if it's a Python file
            if content.path.endswith(".js"):
                # save the file
                filename = os.path.join("javascript-files", f"{repo.full_name.replace('/', '-')}-{content.path}")
                with open(filename, "wb") as f:
                    f.write(content.decoded_content)
            print(content)
      
    except Exception as e:
        print("Error:", e)
    
    
# Github username from the command line
username = "Ckudat"
# pygithub object
g = github.Github(input("access token: "))
# get that user by username
user = g.get_user(username)
# iterate over all public repositories
for repo in user.get_repos():
    print_repo(repo)
    print("="*100)