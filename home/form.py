from flask_wtf import Form
from wtforms import validators, StringField, IntegerField
from wtforms.fields import SelectField

class SearchForm(Form):
    price = IntegerField('Price')
    year = IntegerField('Year')
    make = StringField('Make')
    condition = SelectField('Condition', validators=[validators.Optional()])
    cylinder = SelectField('Cylinder', validators=[validators.Optional()])
    fuel = SelectField('Fuel', validators=[validators.Optional()])
    odometer = IntegerField('Odometer')
    size = SelectField('Size', validators=[validators.Optional()])
    title_status = SelectField('Title', validators=[validators.Optional()])
    transimission = SelectField('Transimission', validators=[validators.Optional()])
    type = SelectField('Type', validators=[validators.Optional()])