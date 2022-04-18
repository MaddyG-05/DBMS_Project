from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from mainApp import app

f_src_id=None
f_dest_id=None
f_train_id=None
f_class_type=None

@app.route('/flight1')
def train1():
    return "flight1"

@app.route('flight2')
def train2():
    return 'flight2'

@app.route('flight3')
def train3():
    return 'flight3'