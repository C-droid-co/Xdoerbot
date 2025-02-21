import tweepy
import os
import schedule
import time
from dotenv import load_dotenv
from news import fetch_and_post_news
from health import fetch_and_post_health
from musk import fetch_and_post_musk
from responses import check_mentions
from greetings import post_greeting
from utils import post_tweet

# Load API keys
load_dotenv()

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(
    os.getenv('API_KEY'),
    os.getenv('API_SECRET'),
    os.getenv('ACCESS_TOKEN'),
    os.getenv('ACCESS_TOKEN_SECRET')
)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Creator handle
CREATOR = os.getenv('CREATOR_HANDLE')

# Schedule tasks (adjusted for Twitter's free plan: 500 posts/month, ~16/day)
schedule.every(12).hours.do(lambda: fetch_and_post_news(api, post_tweet, CREATOR))  # 2 news posts/day
schedule.every(24).hours.do(lambda: fetch_and_post_health(api, post_tweet, CREATOR))  # 1 health post/day
schedule.every(24).hours.do(lambda: fetch_and_post_musk(api, post_tweet, CREATOR))  # 1 Musk post/day
schedule.every(12).hours.do(lambda: check_mentions(api, CREATOR))  # 2 checks/day, ~2 replies/day
schedule.every(24).hours.do(lambda: post_greeting(api, post_tweet, CREATOR))  # 1 greeting/day

# Run the bot
print("X News Bot is running...")
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
