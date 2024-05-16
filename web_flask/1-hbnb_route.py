#!/usr/bin/python3
"""This module starts a Flask web application."""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """The hello route displays 'Hello HBNB!' when accessed."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """The hbnb route displays 'HBNB' when accessed"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
