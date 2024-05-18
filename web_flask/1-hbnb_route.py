#!/usr/bin/python3
"""a script that starts a Flask web application
listening on 0.0.0.0, port 5000"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    This function is the home route of the Flask application.

    Returns:
        str: The string "Hello HBNB!" as the response to the home route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function is the home route of the Flask application.

    Returns:
        str: The string "HBNB!" as the response to the hbnb route.
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
