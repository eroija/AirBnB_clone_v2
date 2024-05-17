#!/usr/bin/python3
"""This module starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Fetches data from storage engine and displays states in an HTML page"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(exception):
    """Closes the session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
