####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

import datetime

from flask import Flask, jsonify, render_template, redirect, url_for, request
from app import app

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

datetime_now_str = str(datetime.datetime.now())

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------
####  API EXAMPLE
####--------------------------------------------------------------------------
####  curl -H "Content-Type: application/json" -X POST http://0.0.0.0:7007/home/
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
@app.route('/', methods=["GET", "POST"])
@app.route('/home/', methods=["GET", "POST"])
def home():
    datetime_now_str = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return 'Wellcome! ' + datetime_now_str

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
