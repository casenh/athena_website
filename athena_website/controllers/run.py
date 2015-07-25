#!/usr/bin/env python

from athena_website import app
from flask import render_template

# Rendering the home page
@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')
