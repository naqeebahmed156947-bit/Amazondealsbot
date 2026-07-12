
import json
import os
import requests

print("Bot started")

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")

if not TOKEN:
    raise Exception("TELEGRAM_TOKEN is missing")

if not CHANNEL:
    raise Exception("TELEGRAM_CHANNEL is missing")

if not os.path.exists("posts.json"):
    raise Exception("posts.json file not found")

with open("posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

print(f"Found {len(posts)} posts")

for post in posts:
    if "text" not in post:
        print("Post skipped: no text found")
        continue

    message = post["text"]

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHANNEL,
        "text": message
    }

    response = requests.post(url, data=data)

    print(response.text)

    if response.status_code != 200:
        print("Failed to send post")

print("Bot finished")
