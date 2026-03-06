import requests
import time
import random
import os
from flask import Flask
import threading

# ==============================
# ENVIRONMENT VARIABLES
# ==============================

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

# ==============================
# SAMPLE DEALS (can replace later)
# ==============================

deals = [
    {
        "name": "Boat Airdopes 141",
        "price": "₹1299",
        "discount": "55%",
        "link": "https://amzn.to/testdeal1"
    },
    {
        "name": "Noise Smartwatch",
        "price": "₹1999",
        "discount": "60%",
        "link": "https://amzn.to/testdeal2"
    },
    {
        "name": "Samsung Powerbank",
        "price": "₹899",
        "discount": "50%",
        "link": "https://amzn.to/testdeal3"
    }
]

# ==============================
# TELEGRAM MESSAGE SENDER
# ==============================

def send_deal(deal):

    message = f"""
🔥 DEAL ALERT 🔥

🛍 Product: {deal['name']}
💰 Price: {deal['price']}
🎯 Discount: {deal['discount']}

⭐ Best Deal Today

👉 Buy Now:
{deal['link']}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHANNEL_USERNAME,
        "text": message
    }

    requests.post(url, data=payload)


# ==============================
# TELEGRAM DEAL LOOP
# ==============================

def deal_loop():
    while True:
        deal = random.choice(deals)
        send_deal(deal)
        time.sleep(3600)  # 1 hour


# ==============================
# FLASK SERVER FOR RENDER
# ==============================

app = Flask(__name__)

@app.route("/")
def home():
    return "DealsYeti Bot Running"


def run_web():
    app.run(host="0.0.0.0", port=10000)


# ==============================
# START EVERYTHING
# ==============================

threading.Thread(target=run_web).start()
threading.Thread(target=deal_loop).start()
