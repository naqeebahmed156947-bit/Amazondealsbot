
import json
import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")

with open("posts.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

for post in posts:
    message = post["text"]

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHANNEL,
        "text": message
    }

    requests.post(url, data=data)
