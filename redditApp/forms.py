from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class SearchForSubredditForm(FlaskForm):
    search = StringField('Search for subreddit',\
                         validators=[DataRequired()])
     submit = SubmitField('Search')