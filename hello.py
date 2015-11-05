import os
from flask import Flask, request

import astropy
print astropy.__version__

app = Flask(__name__)

@app.route('/')
def hello():
    return "<img src='static/ILTU_white.png'>"

@app.route('/dotastro7')
def hello():
    return open(dotastro7.html)

if __name__ == '__main__':
    app.run()


