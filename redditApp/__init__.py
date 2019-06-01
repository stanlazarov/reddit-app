from flask import Flask
import praw

app = Flask(__name__)
app.config['SECRET_KEY'] = '9cf59f956022a026f61b7ba347ae824d'

reddit = praw.Reddit(client_id='LHmmSkweyzSiAA', \
                     client_secret='Zs2_1an3ELAMSKaB-ewFpkr8TjQ', \
                     user_agent='Praw project for uni v1.0 by /u/praw_test123', \
                     username='praw_test123')
                     #password='pr4wT3st')

from redditApp import routes
