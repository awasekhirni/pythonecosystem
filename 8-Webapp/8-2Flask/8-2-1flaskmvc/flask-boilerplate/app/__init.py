########################################
# Copyright 2013-19 Dr. Syed Awase Khirni
#      TPRI/SYCLIQ CORPORATION
#      BANGALORE, INDIA
# FLASK MICROFRAMEWORK BOILER PLATE WITH BOOTSTRAP 
#       LAST UPDATED ON MARCH 2019
# OPEN FOR USE PROVIDED YOU TWEET AND ACKNOWLEDGE IN TWITTER AND LINKEDIN
# SHOULD YOU HAVE ANY UPDATES OR MODIFICATIONS PLEASE DO ADD AND UPDATE THEM WITH YOUR SIGNATURE/EMAIL ADDRESS
#####################################################

import os.path
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask_moment import Moment
#for postgresql 
import psycopg2




basedir = os.path.abspath(os.path.dirname(__file__))


app=Flask(__name__,template_folder='../templates', static_folder='../static')
#open the python shell 
# run the following commands 
# import os 
# os.urandom(24)
#now lets add this as secret key
APP_SECRET_KEY = os.urandom(256); 
app.config['SECRET_KEY'] = APP_SECRET_KEY


########################################################
#DATABASE CONFIGURATION SECTION
#SQLAlchemy Configurations

#SQLITE Database Configurations
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'boilerplateprj.db')


#MongoDB Configurations 
# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
# mongo = PyMongo(app)
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'siebenflaskdb',
#     'host':'127.0.0.1',
#     'port':12345,
#     #'username':'webapp',
#     #'password':'pwd123'
# }




#Postgresql Database Configurations 
POSTGRES = {
    'user': 'postgres',
    'password': 'dbp@ssw0rd',
    'db': 'siebenflaskdb',
    'host': '127.0.0.1',
    'port': '5432',
}



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s' % POSTGRES


#MYSQL Database Configurations 
# MYSQL={
#     'user': 'mysql',
#     'password': 'password',
#     'db': 'boilerplatedb',
#     'host': 'localhost',
#     'port': '3306',
# }
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s' % MYSQL

#ORACLE DATABASE CONFIGURATIONS 


#COUCHDB CONFIGURATIONS 



#enable and disable SQLAlchemy to track modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#############################################

#app
app.config['DEBUG'] =True
#initializing SQLAlchemy 
db = SQLAlchemy(app)

###############################################

# #Authentication Configuration 
login_manager=LoginManager()
login_manager.session_protection= "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

##################################################
#for displaying timestamps 
moment =Moment(app)

#################################################
# Bootstrap CONFIGURATION
from flask_bootstrap import Bootstrap
Bootstrap(app)

##################################################
#configuration of the debug toolbar 
from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension(app)

###########################################

import doctorappointmentapp.models 
import doctorappointmentapp.controllers 
import doctorappointmentapp.filters
