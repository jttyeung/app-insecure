""" App Insecure Server """

from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension

import jinja2
import os


app = Flask(__name__)

app.secret_key = os.environ['APPINSECURE_KEY']

# jinja debugger
app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True



@app.route('/')
def homepage():
    """ Brings user to the homepage. """
    return render_template('index.html')


@app.route('/levelzero')
def level_zero():
    """ Brings user to the first level of the game. """
    return render_template('levelzero.html')


@app.route('/levelone')
def level_one():
    """ Brings user to the first level of the game. """
    return render_template('levelone.html')


@app.route('/levelonejk')
def level_one_jk():
    """ Brings user to the fake first level of the game. """
    username = request.args.get('username')
    password = request.args.get('password')

    return render_template('level1.html', username=username, password=password)


@app.route('/leveltwo')
def level_two():
    """ Brings user to the second level of the game. """


    return render_template('level1.html', username=username, password=password)





if __name__ == "__main__":
    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    # Connect DB to Flask before running app
    # connect_to_db(app)

    app.run(host="0.0.0.0", port=5000)
