import os
import telebot
from flask import Flask, request

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('القناة 📢', url='https://t.me/zzicu')
    btn2 = telebot.types.InlineKeyboardButton('البوتات 🤖', callback_data='bots')
    markup.add(btn1, btn2)
    
    bot.reply_to(message, f"""أهلاً بك {message.from_user.first_name} 💙

أنا بوت قناة @zzicu 
كل يوم بوت مدفوع صار مجاني 🔥

👇 اشترك بالقناة عشان يوصلك كل جديد""", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "وصلني كلامك يا كيان 😂🔥\n\nارسل /start عشان تشوف القائمة")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "bots":
        bot.answer_callback_query(call.id, "قائمة البوتات قريباً...")

@app.route('/', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route('/')
def index():
    return "البوت شغال تمام ✅"

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url='https://kayan-bot.onrender.com/') 
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
