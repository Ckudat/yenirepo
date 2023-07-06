# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 15:26:09 2023

@author: monster
"""

import requests
from pprint import pprint

# github username
username = "Ckudat"
# url to request
url = f"https://api.github.com/users/Ckudat"
# make the request and return the json
user_data = requests.get(url).json()
# pretty print JSON data
pprint(user_data)