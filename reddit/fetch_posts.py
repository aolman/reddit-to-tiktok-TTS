import praw
import json

VIDEO_DURATION_LIMIT = 120

def get_reddit_client():
    with open("config/settings.json") as f:
        creds = json.load(f)["reddit"]
    return praw.Reddit(
        client_id=creds["client_id"],
        client_secret=creds["client_secret"],
        user_agent=creds["user_agent"]
    )
    
def estimate_narration_time(text, words_per_minute=180):
    words = len(text.split())
    return words / (words_per_minute / 60)

def fetch_posts(subreddit="AmITheAsshole", max_posts=20):
    reddit = get_reddit_client()
    posts = reddit.subreddit(subreddit).top(time_filter="day",limit=max_posts)
    for post in posts:
        title = post.title
        body = post.selftext if post.selftext else ""
        full_text = title + "\n" + body
        estimated_time = estimate_narration_time(full_text)
        if estimated_time < VIDEO_DURATION_LIMIT:
            return {
                "title": post.title,
                "body": body,
            }
    raise Exception("No suitable post found under time limit.")