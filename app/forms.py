from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError



class FlickrForm(FlaskForm):
    title = StringField('Search Flickr', validators=[DataRequired()])
    submit  = SubmitField('Submit')
