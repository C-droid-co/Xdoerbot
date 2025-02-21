import tweepy
import random
import time

RESPONSES = [
    "Hey {}, thanks for the shoutout! What’s on your mind? #XBot by {}",
    "Hi {}, glad you mentioned me! How can I assist? #XBot by {}",
    "Yo {}, love the mention! Any news you want to share? #XBot by {}"
]

def check_mentions(api, creator):
    try:
        mentions = api.mentions_timeline(count=5)  # Limited to 5 reads/day
        reply_count = 0
        for mention in mentions:
            if not mention.favorited and reply_count < 2:  # Limit to 2 replies/day
                api.create_favorite(mention.id)
                response = random.choice(RESPONSES).format(mention.user.screen_name, creator)
                api.update_status(response, in_reply_to_status_id=mention.id)
                print(f"Replied to {mention.user.screen_name}")
                reply_count += 1
                time.sleep(60)  # Avoid rate limits
    except tweepy.TweepError as e:
        print(f"Error responding to mention: {e}")
        time.sleep(60)
