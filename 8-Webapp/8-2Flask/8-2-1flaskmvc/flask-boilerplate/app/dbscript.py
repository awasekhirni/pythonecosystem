from flask import current_app 
from flask_script import Command 


from doctorappointmentapp.models import *

def ResetDB(Command):
    """Drops all tables in the database and recreates them""" 
    print("We are going to drop the collections from MongoDB")



def PopulateDB(Command):
    """Drops all tables in the database and recreates them""" 
    print("We are going to populate the MongoDB")
