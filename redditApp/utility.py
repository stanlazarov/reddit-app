import datetime, time

def get_time_elapsed(submission):
    created_unix = submission.created_utc
    now_unix = time.mktime(datetime.datetime.now().timetuple())
    sec_elapsed = int(now_unix - created_unix)
    if sec_elapsed < 60:
        return str(sec_elapsed) + ' seconds'
    min_elapsed = sec_elapsed // 60
    if min_elapsed < 60:
        return str(min_elapsed) + ' minutes' 
    hours_elapsed = min_elapsed // 60
    if hours_elapsed < 24:
        return str(hours_elapsed) + ' hours'
    days_elapsed = hours_elapsed // 24
    return str(days_elapsed) + ' days'
