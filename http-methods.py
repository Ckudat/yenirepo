# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:26:29 2023

@author: monster
"""

from flask import request
from flask import Flask

ilkproje = Flask(__name__)
@ilkproje.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
if __name__ == '__main__':
    ilkproje.run(debug=False)        