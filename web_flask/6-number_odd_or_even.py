#!/usr/bin/python3
""" script that starts a Flask web application"""
from flask import Flask, render_template


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
@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    """ displays n followed by the variable text """
    if type(n) is int:
        text = n + " is a number"
    return text


@app.route('/number_template/', strict_slashes=False)
@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n):
    """ displays HTML  """
    if type(n) is int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/', strict_slashes=False)
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_template(n):
    """ displays HTML  """
    if type(n) is int:
        return render_template('6-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
