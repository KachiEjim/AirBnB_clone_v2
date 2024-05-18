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
        str: The string "Hello HBNB!" as the response
        to the home route.
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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
        This function is the route for the '/c/<text>'
        endpoint of the Flask application.

        Parameters:
            text (str): The text parameter extracted from the URL.

        Returns:
            str: The string "C " concatenated with the
            text parameter after replacing underscores with spaces.
    """
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    This function is the route for the '/python/' and
    '/python/<text>' endpoints of the Flask application.

    Parameters:
        text (str): The text parameter extracted
        from the URL. Defaults to 'is cool' if not provided.

    Returns:
        str: The string "Python " concatenated
        with the text parameter after replacing underscores with spaces.
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """
    This function is the route for the
    '/number/<n>' endpoint of the Flask application.

    Parameters:
        n (str): The n parameter extracted from the URL.

    Returns:
        str: The string "{n} is a number"
        if n is a valid number, otherwise None.
    """
    return f"{n} is a number"


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """
    This function is the route for the
    '/number/<n>' endpoint of the Flask application.

    Parameters:
        n (str): The n parameter extracted from the URL.

    Returns:
        H1 tag: “Number: n” inside the tag BODY
    """
    return f"<h1>Number: {n}</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
