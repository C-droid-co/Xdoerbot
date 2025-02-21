import random

GREETINGS = [
    "Good morning, X fam! Rise and shine, it’s news time! #GoodVibes by {}",
    "Good afternoon, folks! Hope your day’s as awesome as this bot! #Cheers by {}",
    "Good evening, buddies! Time to unwind with some updates! #NightMode by {}"
]

def post_greeting(api, post_tweet, creator):
    greeting = random.choice(GREETINGS).format(creator)
    post_tweet(greeting)
