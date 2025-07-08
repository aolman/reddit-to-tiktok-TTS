import praw
import json

def get_reddit_client():
    with open("config/settings.json") as f:
        creds = json.load(f)["reddit"]
    return praw.Reddit(
        client_id=creds["client_id"],
        client_secret=creds["client_secret"],
        user_agent=creds["user_agent"]
    )
    
def fetch_posts(subreddit="AskReddit", limit=1):
    reddit = get_reddit_client()
    posts = reddit.subreddit(subreddit).top(time_filter="day",limit=limit)
    for post in posts:
        return {
            "title": post.title,
            "body": post.selftext if post.selftext else "[No body text]",
        }