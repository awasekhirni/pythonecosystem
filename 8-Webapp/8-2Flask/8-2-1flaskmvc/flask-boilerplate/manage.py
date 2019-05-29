#! /usr/bin/env python 

from doctorappointmentapp import app, db  
from doctorappointmentapp.models import *
from flask_script import Manager, prompt_bool,Server

manager=Manager(app)

@manager.command
def initdb():
    db.create_all()
    #db.session.add(User(username="syed",email="sak@tpri.com",password="test123"))
    #db.session.add(User(username="rayyan",email="rayyan@tpri.com",password="test123"))
    db.session.commit()
    print("The Database is Initialized!")

@manager.command 
def dropdb():
    if prompt_bool("Are you sure you want o loose all the records in your database"):
        db.drop_all()
        print("The Database has been dropped!!")



if __name__=='__main__':
    manager.add_command('runserver', Server(host='localhost',port=9090))
    manager.run()
