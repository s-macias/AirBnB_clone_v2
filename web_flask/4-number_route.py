#!/usr/bin/python3
""" script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ displays Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_1():
    """ displays HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """ displays C followed by the variable text """
    text = "C " + text.replace('_', ' ')
    return text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_Python(text='is_cool'):
    """ displays python followed by the variable text """
    text = "Python " + text.replace('_', ' ')
    return text


@app.route('/number/', strict_slashes=False)
@app.route('/number/<n>', strict_slashes=False)
def display_n(n):
    """ displays python followed by the variable text """
    if type(n) is int:
        text = n + " is a number"
    return text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
