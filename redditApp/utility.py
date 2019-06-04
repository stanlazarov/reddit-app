import datetime, time, sys
from redditApp import praw, reddit
from prawcore import NotFound
from praw.models import Redditor

def get_time_elapsed(submission):
    created_unix = submission.created_utc
    now_unix = time.mktime(datetime.datetime.now().timetuple())
    sec_elapsed = int(now_unix - created_unix)
    if sec_elapsed < 60:
        return str(sec_elapsed) + (' seconds' if not sec_elapsed == 1 else ' second')
    min_elapsed = sec_elapsed // 60
    if min_elapsed < 60:
        return str(min_elapsed) + (' minutes' if not min_elapsed == 1 else ' minute')
    hours_elapsed = min_elapsed // 60
    if hours_elapsed < 24:
        return str(hours_elapsed) + (' hours' if not hours_elapsed == 1 else ' hour')
    days_elapsed = hours_elapsed // 24
    if days_elapsed < 7:
        return str(days_elapsed) + (' days' if not days_elapsed == 1 else ' day')
    weeks_elapsed = days_elapsed // 7
    if days_elapsed < 30:
        return str(weeks_elapsed) + (' weeks' if not weeks_elapsed == 1 else ' week')
    months_elapsed = days_elapsed // 30
    if days_elapsed < 365:
        return str(months_elapsed) + (' month' if not months_elapsed == 1 else ' month')
    years_elapsed = days_elapsed // 365
    return str(years_elapsed) + ' years'

def get_submission_comments(submission, n):
    comments = []
    i = 1
    for comment in submission.comments:
        if i >= n:
            break
        if isinstance(comment, praw.models.MoreComments):
            continue
        comments.append(comment)
        i += 1
    return comments

def is_valid_comment(comment):
    if isinstance(comment, praw.models.MoreComments):
        return False
    if isinstance(comment, praw.models.comment_forest.CommentForest):
        return False
    return True

def get_redditor_comments(redditor, n):
    comments = []
    i = 1
    for comment in redditor.comments.new():
        if i >= n:
            break
        comments.append(comment)
        i += 1
    return comments

def sub_exists(sub):
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists

def redditor_exists(name):
    exists = True
    try:
        redditor = reddit.redditor(name)
        redditor.created_utc
    except NotFound:
        exists = False
    except TypeError:
        exists = False
    return exists

def format_img_link(link):
    if '?' in link:
        return link.split('?')[0]
    return link