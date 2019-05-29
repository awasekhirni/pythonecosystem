#doctorappointmentapp/controller.py 
from flask import render_template, url_for,redirect,abort,render_template_string
from doctorappointmentapp import app,db


#render view routes here 


@app.route('/')
@app.route('/index',methods=['GET'])
def homepage():
    """ Render the homepage landing page template """ 
    return render_template('home/index.html',title='Welcome to SYCLIQ')
    #return render_template_string("Welcome to SYCLIQ")


@app.route('/dashboard',methods=['GET'])
#@login_required 
def dashboard():
    """ rendering the dashboard template """
    return render_template('home/dashboard.html',title='SycliQ Dashboard')
