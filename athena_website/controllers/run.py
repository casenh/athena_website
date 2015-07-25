#!/usr/bin/env python

from athena_website import app
from flask import render_template

# Rendering the home page
@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

# Rending the data page
@app.route("/data", methods=["GET"])
def get_data():
    print("Routing data")
    return render_template('data.html')

# Collect post information
@app.route("/data", methods=["POST"])
def post_data():
    print("GOT DATA")
    print(request.json)

    # Rending the data page
@app.route("/multi-line", methods=["GET"])
def get_data2():
    print("Routing data")
    return render_template('multi-line.html')

# Collect post information
@app.route("/multi-line", methods=["POST"])
def post_data2():
    print("GOT DATA")
    print(request.json)

        # Rending the data page
@app.route("/multi-line-full", methods=["GET"])
def get_data3():
    print("Routing data")
    return render_template('multi-line-full.html')

# Collect post information
@app.route("/multi-line-full", methods=["POST"])
def post_data3():
    print("GOT DATA")
    print(request.json)