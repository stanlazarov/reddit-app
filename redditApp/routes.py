from redditApp import app, reddit
from redditApp.utility import get_time_elapsed, get_submission_comments, sub_exists, redditor_exists, format_img_link, get_redditor_comments
from redditApp.forms import SearchForSubredditForm, SearchForRedditorForm
from flask import flash, request, redirect, render_template, url_for
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
    comments = get_submission_comments(post, 30)
    img_source = None
    if mimetypes.guess_type(post.url)[0]:
        img_source = post.url
    return render_template('post.html', post=post, img_source=img_source, get_date=get_time_elapsed, comments=comments, title=post.title)

@app.route("/u/<redditor_name>")
def redditor(redditor_name):
    redditor = reddit.redditor(redditor_name)
    comments = get_redditor_comments(redditor, 30)
    avatar_link = format_img_link(redditor.icon_img)
    return render_template('redditor.html', redditor=redditor, get_date=get_time_elapsed, avatar=avatar_link, title=redditor.name, comments=comments)

@app.route("/search/subreddit", methods=['GET', 'POST'])
def search_for_subreddit():
    form = SearchForSubredditForm()
    if form.validate_on_submit():
        if sub_exists(form.search.data):
            return redirect(url_for('open_subreddit', subreddit_name=form.search.data))
        else:
            flash("A subreddit with the name " + "'" + form.search.data + "'" +  " does not exist.", 'danger')
    return render_template('search.html', title='Subreddit search', form=form)

@app.route("/search/redditor", methods=['GET', 'POST'])
def search_for_redditor():
    form = SearchForRedditorForm()
    if form.validate_on_submit():
        if redditor_exists(form.search.data):
            return redirect(url_for('redditor', redditor_name=form.search.data))
        else:
            flash("A redditor with the name " + "'" + form.search.data + "'" +  " does not exist.", 'danger')
    return render_template('search.html', title='Redditor search', form=form)
    