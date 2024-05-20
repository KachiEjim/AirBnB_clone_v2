#!/usr/bin/python3
""" moduleThis module provides utility 
functions for mathematical operations such as
addition, subtraction, multiplication, and division.
""" 
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Renders a template that lists states retrieved from the storage."""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    """ Closes the database connection
    at the end of the request or when the application shuts down. """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
