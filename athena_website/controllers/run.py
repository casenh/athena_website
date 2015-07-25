#!/usr/bin/env python

from athena_website import app
from flask import render_template, request

from . import athenahealthapi

# OAuth information
key = r'6uqkebvamka8r5ra7u7w7hv4'
secret = 'hpHPdcP6agKSmBS'
version = 'preview1'
practiceid = 195900
api = athenahealthapi.APIConnection(version, key, secret, practiceid)

# Rendering the home page
@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

# Rending the data page
@app.route("/data", methods=["GET"])
def get_data():
    return render_template('data.html')

# Collect post information
@app.route("/data", methods=["POST"])
def post_data():
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

    if "json" in request:
        print(request.json)
    return "Ok", 200

@app.route("/d3", methods=["GET"])
def get_d3():
    return render_template('d3.html', data=[1,2,3,4,5,6,7])

# Testing AthenaHealth
@app.route('/login', methods=["GET","POST"])
def get_athena():
    api._authenticate()
    res = api.GET('/practiceinfo')
    print(res)

# Populate a fake patient
@app.route('/populate', methods=["GET"])
def get_populate():
    api._authenticate()
    patient_info = {
    	'lastname': 'Foo',
    	'firstname': 'Jason',
    	'address1': '123 Any Street',
    	'city': 'Cambridge',
    	'countrycode3166': 'US',
    	'departmentid': 1,
    	'dob': '6/18/1987',
    	'language6392code': 'declined',
    	'maritalstatus': 'S',
    	'race': 'declined',
    	'sex': 'M',
    	'ssn': '*****1234',
    	'zip': '02139',
    }
    new_patient = api.POST('/patients', patient_info)
    return("Populated User")
