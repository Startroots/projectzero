from flask import url_for, redirect, render_template, flash, g, session
from flask_login import login_user, logout_user, current_user, login_required
from flask_wtf import FlaskForm
from wtforms  import TextField, TextAreaField, DateTimeField, PasswordField
from wtforms.validators import Required

from datetime import datetime
import pandas as pd

import requests
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager


import os

app = Flask(__name__)

#SECRET_KEY = os.urandom(32)
#app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
	data = pd.read_excel('LinkedIn_intern_jobs_2_chile.xlsx')
	company = list(data['Company'])
	title = list(data['Title'])
	description = list(data['Description'])
	link = list(data['Link'])
	data["Function"]= data["Function"].str.split(", ")
	functions = list(data['Function'])
	final = []
	for x in functions:
		if type(x) == list:
			for i in x:
				i.replace(" ", "")
				final.append(i)
	all_functions = list(set(final))   
	return render_template('index.html', company=company, title=title, description=description, 
	functions=functions, link=link, all_functions=all_functions)

@app.route('/index/')
def index2():
	data = pd.read_excel('LinkedIn_intern_jobs_2_chile.xlsx')
	company = list(data['Company'])
	title = list(data['Title'])
	description = list(data['Description'])
	link = list(data['Link'])
	data["Function"]= data["Function"].str.split(",")
	functions = list(data['Function'])
	final = []
	for x in functions:
		if type(x) == list:
			for i in x:
				i.replace(" ", "")
				final.append(i)
	all_functions = list(set(final))   
	return render_template('index.html', company=company, title=title, description=description, 
	functions=functions, link=link, all_functions=all_functions)
	#return render_template('index.html')

# ====================



if __name__ == "__main__":
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)