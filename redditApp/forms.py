from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForSubredditForm(FlaskForm):
    search = StringField('Search for subreddit', validators=[DataRequired()])
    submit = SubmitField('Search')