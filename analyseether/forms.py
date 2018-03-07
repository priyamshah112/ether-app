from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email
from wtforms import StringField


class Form(FlaskForm):
    email = StringField('Email',
                    validators=[InputRequired("Please enter a non-empty email address."),
                                Email("Please enter a proper email address.")],
                    render_kw={"placeholder": "Enter your email and subscribe to our newsletter"})
