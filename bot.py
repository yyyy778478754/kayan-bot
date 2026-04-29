from flask import Flask, request
import requests

TOKEN = "8703354892:AAFp_T3Tx_f7_e4LZeUOB78w55VgiMWchfE"
app = Flask(__name__)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text == "/start":
            send_message(chat_id, "اشتغلنا على Render 🚀 فل يا كيان")
        else:
            send_message(chat_id, f"كتبت: {text}")
    return "ok"
