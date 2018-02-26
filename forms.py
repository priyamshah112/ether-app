from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import EmailField

class Form(FlaskForm):
    email = EmailField('Email', validators=[InputRequired("Please enter your email address."), Email("Please enter proper email address.")], render_kw={"placeholder": "Please Enter Email Address"})
