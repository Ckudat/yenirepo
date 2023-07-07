# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:33:00 2023

@author: monster
"""
from flask import Flask
from flask import request
from flask import render_template
ilkproje = Flask(__name__)
@ilkproje.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
"16. ve 18. satırlarda valid_login ve log_the_user_in kısımları çıktı alabildikten sonra incelenecek ve düzenlenecek"