from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, DateTimeField, PasswordField, validators, StringField
from wtforms.validators import Required, DataRequired, Email
import email_validator

class ExampleForm(FlaskForm):
	#title = TextField(u'Title', validators = [Required()])
	#title = TextAreaField(u'Title', validators = [Required()])
	nickname = StringField(u'Nickname')
	#amount_paid = IntegerField(u'Monto a pagar')
	email = StringField(u'Email', validators=[Email()])
	#date = DateTimeField(u'Date', format='%d/%m/%Y %H:%M')
	#recaptcha = RecaptchaField(u'Recaptcha')

class LoginForm(FlaskForm):
	user = TextField(u'User', validators = [Required()])
	password = PasswordField(u'Password', validators = [Required()])
