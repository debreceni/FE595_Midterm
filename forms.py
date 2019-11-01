from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class SentimentForm(FlaskForm):
    text = StringField('Enter Text Below:', validators=[DataRequired()])
    submit = SubmitField('Enter')