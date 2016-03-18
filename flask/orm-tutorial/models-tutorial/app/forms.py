from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import *

class CustomerForm(Form):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last name', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    zipcode = StringField('Zip Code', validators=[DataRequired()])

class OrderForm(Form):
    name = StringField('Order name', validators=[DataRequired()])
    cost = StringField('Total Cost', validators=[DataRequired()])
    parts = StringField('Number of Parts', validators=[DataRequired()])

# class AddressForm(Form):
