from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from functions import SPACY_POS_MAPPING


class SentimentForm(FlaskForm):
    class Meta:
        csrf = False
    text = StringField('Enter Text Below:', validators=[DataRequired()])
    submit = SubmitField('Enter')


class POSForm(FlaskForm):
    class Meta:
        csrf = False
    text = StringField("Enter Text Below", validators=[DataRequired()])
    tags = list(SPACY_POS_MAPPING.keys())
    tag = SelectField('Tag', choices=[(tag, tag) for tag in tags], validators=[DataRequired()])
    submit = SubmitField('Enter')


class SimilarityForm(FlaskForm):
    class Meta:
        csrf = False
    text1 = StringField("Enter First Text Below", validators=[DataRequired()])
    text2 = StringField("Enter Second Text Below", validators=[DataRequired()])
    submit = SubmitField('Enter')
