# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:28:54 2023

@author: monster
"""

from flask import render_template
from flask import Flask

ilkproje = Flask(__name__)
@ilkproje.route('/hello/')
@ilkproje.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
if __name__ == '__main__':
    ilkproje.run(debug=False)        