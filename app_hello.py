import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# -----CONNECTIONS
engine = create_engine("sqlite:///hawaii.sqlite")


# reflect the database into classes
Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


# Create a New Flask App Instance

# This __name__ variable denotes the name of the current function. 
# You can use the __name__ variable to determine if your code is being run from the command line or 
# if it has been imported into another piece of code. Variables with underscores before and after them are called magic methods in Python.
app = Flask(__name__)

@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')