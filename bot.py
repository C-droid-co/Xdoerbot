import tweepy
import os
import schedule
import time
import http.server
import socketserver

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

# Schedule tasks
schedule.every(12).hours.do(lambda: fetch_and_post_news(api, post_tweet, CREATOR))
schedule.every(24).hours.do(lambda: fetch_and_post_health(api, post_tweet, CREATOR))
schedule.every(24).hours.do(lambda: fetch_and_post_musk(api, post_tweet, CREATOR))
schedule.every(12).hours.do(lambda: check_mentions(api, CREATOR))
schedule.every(24).hours.do(lambda: post_greeting(api, post_tweet, CREATOR))

# Start a simple HTTP server on port 10000 to satisfy Render's port check
PORT = 10000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    # Run the bot in a separate thread or background while keeping the server alive
    import threading
    bot_thread = threading.Thread(target=lambda: exec(open("bot.py").read()), daemon=True)
    bot_thread.start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

# Original bot loop (if not using the server approach)
print("X News Bot is running...")
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
