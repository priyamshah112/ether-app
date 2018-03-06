from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email
from wtforms import StringField


class Form(FlaskForm):
    email = StringField('Email',
                    validators=[InputRequired("Please enter your email address."),
                                Email("Please enter proper email address.")],
                    render_kw={"placeholder": "Please Enter Email Address"})
