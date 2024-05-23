#!/usr/bin/python3
""" module doc """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def hbnb2():
    """ def doc """
    path = '100-hbnb.html'
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template(path, states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def close(error):
    """ def doc """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
