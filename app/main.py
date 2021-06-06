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
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager


import os

"""class ExampleForm(FlaskForm):
	#title = TextField(u'Title', validators = [Required()])
	title = TextAreaField(u'Title', validators = [Required()])
	content = TextAreaField(u'Content')
	date = DateTimeField(u'Date', format='%d/%m/%Y %H:%M')
	#recaptcha = RecaptchaField(u'Recaptcha')
"""


app = Flask(__name__)
bootstrap = Bootstrap(app) 

#SECRET_KEY = os.urandom(32)
#app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
	data = pd.read_excel('LinkedIn_intern_jobs_2_chile.xlsx')
	company = list(data['Company'])
	title = list(data['Title'])
	description = list(data['Description'])
	functions = list(data['Function'])
	link = list(data['Link'])
	return render_template('index.html', company=company, title=title, description=description, 
	functions=functions, link=link)
	#return render_template('index.html')

@app.route('/index/')
def index2():
	data = pd.read_excel('LinkedIn_intern_jobs_2_chile.xlsx')
	company = list(data['Company'])
	title = list(data['Title'])
	description = list(data['Description'])
	functions = list(data['Function'])
	link = list(data['Link'])
	return render_template('index.html', company=company, title=title, description=description, 
	functions=functions, link=link)
	#return render_template('index.html')

@app.route('/pago/', methods=['GET', 'POST'])
def pago():
	return render_template('pago.html')

@app.route('/error/', methods=['GET', 'POST'])
def error():
	return render_template('error.html')

@app.route("/tables")
def show_tables():
	data = pd.read_excel('LinkedIn_intern_jobs_2_chile.xlsx')
	company = list(data['Company'])
	title = list(data['Title'])
	description = list(data['Description'])
	functions = list(data['Function'])
	link = list(data['Link'])
	return render_template('index.html', company=company, title=title, description=description, 
	functions=functions, link=link)

# ====================
@app.errorhandler(500)
def server_error(e):
    logging.exception("An error occurred during a request.")
    return (
        """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(
            e
        ),
        500,
    )


if __name__ == "__main__":
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)