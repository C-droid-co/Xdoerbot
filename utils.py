from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def post_tweet(message):
    try:
        api.update_status(message)
        print("Tweet posted:", message)
    except tweepy.TweepError as e:
        print(f"Error posting tweet: {e}")
        raise
