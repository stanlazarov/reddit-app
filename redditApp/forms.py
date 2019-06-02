from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from redditApp.utility import sub_exists, redditor_exists

class SearchForSubredditForm(FlaskForm):
    search = StringField('Search for subreddit', validators=[DataRequired()])
    submit = SubmitField('Search')

class SearchForRedditorForm(FlaskForm):
    search = StringField('Search for redditor', validators=[DataRequired()])
    submit = SubmitField('Search')