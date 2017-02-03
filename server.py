""" Web Insecure Server """

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

import jinja2


app = Flask(__name__)





if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
