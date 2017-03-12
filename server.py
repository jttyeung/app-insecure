""" App Insecure Server """

from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
import jinja2


app = Flask(__name__)

# jinja debugger
app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True

@app.route('/')
def homepage():
    """ Brings user to the homepage. """
    return render_template("index.html")


@app.route('/levelzero')
def levelzero():
    """ Brings user to the homepage. """
    return render_template("levelzero.html")


if __name__ == "__main__":
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port=4000)
