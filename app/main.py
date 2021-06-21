from flask import url_for, redirect, render_template, flash, g, session
from flask_login import login_user, logout_user, current_user, login_required
from flask_wtf import FlaskForm
from wtforms  import TextField, TextAreaField, DateTimeField, PasswordField
from wtforms.validators import Required


from wtforms import widgets, SelectMultipleField

from datetime import datetime
import pandas as pd
import numpy as np
import requests
import json
import random


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager


app = Flask(__name__)

SECRET_KEY = os.urandom(32)
#SECRET_KEY = 'development'
app.config['SECRET_KEY'] = SECRET_KEY

def data():
	data = pd.read_excel('LinkedIn_intern_jobs_2_chile.xlsx')
	data["Function"]= data["Function"].str.split(", ")
	functions = list(data['Function'])
	final = []
	for x in functions:
		if type(x) == list:
			for i in x:
				i.replace(" ", "")
				final.append(i)
	all_functions = list(set(final)) 
	return all_functions

def filter(company, title, description,link,link_picture,functions, selection):
	c = []
	t = []
	d = []
	l = []
	lp = []
	f = []
	for i in range(len(company)):
		if type(functions[i]) == list:
			if any(x in selection for x in functions[i]):
				c.append(company[i])
				t.append(title[i])
				d.append(description[i])
				l.append(link[i])
				lp.append(link_picture[i])
				f.append(functions[i])
			elif len(selection)==0:
				c.extend(company)
				t.extend(title)
				d.extend(description)
				l.extend(link)
				lp.extend(link_picture)
				f.extend(functions)
	return c,t,d,l,lp,f

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class SimpleForm(FlaskForm):
    #string_of_files = ['one\r\ntwo\r\nthree\r\n']
    list_of_files = data()
    # create a list of value/description tuples
    files = [(x, x) for x in list_of_files]
    example = MultiCheckboxField('Label', choices=files)

@app.route('/jobs', methods=['post','get'])
def jobs():
	form = SimpleForm()

	data = pd.read_excel('LinkedIn_intern_jobs_2_chile.xlsx')
	company = list(data['Company'])
	title = list(data['Title'])
	description = list(data['Description'])
	link = list(data['Link'])
	link_picture = list(data['Link_picture'])
	data["Function"]= data["Function"].str.split(", ")
	functions = list(data['Function'])
	final = []
	for x in functions:
		if type(x) == list:
			for i in x:
				i.replace(" ", "")
				final.append(i)
	all_functions = list(set(final))   

	#formulario
	if form.validate_on_submit():
		selections = form.example.data
		print(form.example.data)
		company, title, description,link,link_picture,functions = filter(company, title, description,link,link_picture,functions, selections)
		return render_template('jobs.html', company=company, title=title, description=description, 
	functions=functions, link=link, link_picture=link_picture, all_functions=all_functions, form=form)
	else:
		print("error")

	return render_template('jobs.html', company=company, title=title, description=description, 
	functions=functions, link=link, link_picture=link_picture, all_functions=all_functions, form=form)


@app.route('/',methods=['post','get'])
def index():
	filenames = os.listdir("static/img/occupation/png") #read names fies
	filenames = np.array(filenames) #transform to numpy array
	filenames = np.random.permutation(filenames) #positions permutations
	
	files = []
	for i in range(len(filenames)):
		files.append('img/occupation/png/'+filenames[i])

	files = files[:5] #return de first fives


	return render_template('index.html', files=files)
	

if __name__ == "__main__":
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)