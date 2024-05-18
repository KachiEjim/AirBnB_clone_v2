#!/usr/bin/python3
"""a script that starts a Flask web application
listening on 0.0.0.0, port 5000"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)



@app.route('/', strict_slashes=False)
def index():
    """ Route to display all objects from storage """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('states_list.html', states=sorted_states)

@app.teardown_appcontext
def teardown_db(exception):
    """ Closes the storage app context """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
