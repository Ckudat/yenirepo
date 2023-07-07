# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:05:48 2023

@author: monster
"""
from flask import Flask
from flask import url_for
ilkproje = Flask(__name__)

@ilkproje.route("/")
def index():
    return 'index'

@ilkproje.route('/login')
def login():
    return 'login'

@ilkproje.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with ilkproje.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))