from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from mainApp import app

b_src_id=None
b_dest_id=None
b_train_id=None

@app.route('/bus1')
def bus1():
    return "bus1"

@app.route('bus2')
def bus2():
    return 'bus2'

@app.route('bus3')
def bus3():
    return 'bus3'