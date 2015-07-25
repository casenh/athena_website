#!/usr/bin/env python

import flask
import os

# Set up the Flask application
_base = os.path.join(os.path.dirname(__file__), os.path.pardir)
app = flask.Flask("viewer",
        static_folder=os.path.join(_base, "static"),
        template_folder=os.path.join(_base, "templates"))
app.config.from_object("athena_website.config")

# Add the controllers for routing webpages
from . import controllers

# Start the app
app.run(host="ljtrust.org", port=3000)
