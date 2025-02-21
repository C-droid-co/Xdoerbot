import tweepy
import random
import time

MUSK_ACCOUNTS = ["elonmusk", "Tesla"]

def fetch_and_post_musk(api, post_tweet, creator):
    try:
        account = random.choice(MUSK_ACCOUNTS)
        tweets = api.user_timeline(screen_name=account, count=1, exclude_replies=True, include_rts=False)
        if tweets:
            tweet = tweets[0]
            message = f"{tweet.text} (via @{account}) | #ElonMusk #Tesla by {creator}"
            post_tweet(message)
    except tweepy.TweepError as e:
        print(f"Error fetching Musk update from @{account}: {e}")
        time.sleep(60)  # Wait to avoid rate limits
