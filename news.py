import tweepy
import random
import time

# List of news accounts (expand as needed, up to 50+)
NEWS_ACCOUNTS = [
    "CNN", "BBCNews", "Reuters", "nytimes", "AP", "WSJ", "ABC", "NBCNews",
    "CBSNews", "FoxNews", "USATODAY", "TIME", "NPR", "Bloomberg", "WashPost",
    "thehill", "politico", "GuardianUS", "latimes", "Newsweek",
    "CNBC", "Forbes", "BusinessInsider", "HuffPost", "Slate", "Vox", "Axios",
    "AlJazeera", "SkyNews", "MSNBC", "NatGeo", "Economist", "NewYorker",
    "Atlantic", "BuzzFeedNews", "ProPublica", "PBSNewsHour", "CNET", "TechCrunch",
    "Wired", "ArsTechnica", "TheVerge", "Engadget", "Mashable", "Gizmodo",
    "FastCompany", "Inc", "Entrepreneur", "HarvardBiz", "TEDTalks", "NASA"
]

def fetch_and_post_news(api, post_tweet, creator):
    # Cache last fetched tweet to minimize reads
    try:
        account = random.choice(NEWS_ACCOUNTS)
        tweets = api.user_timeline(screen_name=account, count=1, exclude_replies=True, include_rts=False)
        if tweets:
            tweet = tweets[0]
            message = f"{tweet.text} (via @{account}) | #NewsUpdate #XBot by {creator}"
            post_tweet(message)
    except tweepy.TweepError as e:
        print(f"Error fetching news from @{account}: {e}")
        time.sleep(60)  # Wait to avoid rate limits
