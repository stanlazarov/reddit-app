from redditApp import app, reddit
from redditApp.utility import get_time_elapsed, get_comments
from flask import flash, redirect, render_template, url_for
import mimetypes

@app.route("/")
@app.route('/home')
def home():
    posts = reddit.front.hot(limit=30)
    return render_template("home.html", posts=posts, title="Home", get_date=get_time_elapsed)

@app.route("/r/<subreddit_name>")
def open_subreddit(subreddit_name):
    posts = reddit.subreddit(subreddit_name).hot(limit=30)
    return render_template("home.html", posts=posts, title=subreddit_name, get_date=get_time_elapsed)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route('/post/<post_id>')
def post(post_id):
    post = reddit.submission(id=post_id)
    comments = get_comments(post, 30)
    img_source = None
    if mimetypes.guess_type(post.url)[0]:
        img_source = post.url
    return render_template('post.html', post=post, img_source=img_source, get_date=get_time_elapsed, comments=comments)

@app.route("/u/<redditor_name>")
def redditor(redditor_name):
    redditor = reddit.redditor(redditor_name)
    return render_template('redditor.html', redditor=redditor, get_date=get_time_elapsed)
