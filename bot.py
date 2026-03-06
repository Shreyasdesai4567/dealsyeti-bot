import requests
import time
import random

BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN"
CHANNEL_USERNAME = "@DealsYeti"

deals = [
{
"title":"🔥 Boat Airdopes 141",
"price":"₹399",
"link":"https://amzn.to/testdeal",
"discount":"72%"
},
{
"title":"🔥 Noise Smartwatch",
"price":"₹1299",
"link":"https://amzn.to/testdeal",
"discount":"55%"
}
]

def send_deal(deal):

    message = f"""
🔥 {deal['discount']} OFF

🛒 {deal['title']}

💰 Price: {deal['price']}

⭐ Best Deal Today

Buy Now 👇
{deal['link']}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHANNEL_USERNAME,
        "text": message
    }

    requests.post(url, data=payload)

while True:

    deal = random.choice(deals)

    send_deal(deal)

    time.sleep(3600)
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "DealsYeti Bot Running"

def run_web():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_web).start()
