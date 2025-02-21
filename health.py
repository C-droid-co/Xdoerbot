import random

HEALTH_TIPS = [
    "Drink 8 glasses of water daily for optimal hydration!",
    "Take a 30-minute walk to boost your mood and health.",
    "Eat more fruits and veggies for a stronger immune system.",
    "Get 7-8 hours of sleep for better mental clarity.",
    "Practice mindfulness to reduce stress and anxiety."
]

def fetch_and_post_health(api, post_tweet, creator):
    tip = random.choice(HEALTH_TIPS)
    message = f"Daily Health Tip: {tip} | #Health #Wellness by {creator}"
    post_tweet(message)
