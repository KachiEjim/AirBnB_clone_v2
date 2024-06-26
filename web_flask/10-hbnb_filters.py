#!/usr/bin/python3
""" module doc """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ def doc """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ def doc """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ def doc """
    return 'c {}'.format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ def doc """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ def doc """
    return '{} is a number'.format(n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ def doc """
    if n % 2 == 0:
        p = 'even'
    else:
        p = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, parity=p)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ def doc """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ def doc """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_route(id=None):
    """ A script that starts a Flask web application. """
    states = storage.all(State)
    if id:
        state = next((state for state in states.values()
                      if state.id == id), None)
        if state:
            return render_template('9-states.html', state=state, id='Found')
        else:
            return render_template('9-states.html', state=None, id='Not_Found')
    else:
        return render_template('9-states.html', states=states, id='None')


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ def doc """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def close(error):
    """ def doc """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
