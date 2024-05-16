#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Route for the root directory that returns a hello."""
    return 'HELLO HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route for '/hbnb' that returns the string "HBNB"."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route for '/c/<text>' that returns "C" followed by the value of the
    text variable.
    """
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
