from flask import Flask, render_template, make_response, url_for, request, redirect
import copy as cp
import json
# from flask_firebase import FirebaseAuth
# import firebase_admin.auth as auth
# import firebase_admin
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import ee
import numpy as np
import cv2
import cgi
import csv
import requests
import pandas as pd
import seaborn as sns
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import pprint
# import pandas as pd
import calendar
from math import sqrt
# import pandas as pd 
from datetime import datetime
from dateutil import tz

# from meteostat import Point, Daily

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)
# db.create_all()
# db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')