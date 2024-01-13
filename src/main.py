from logging import debug
import telebot
from telebot import types

from service import TopicsService
from config import DEBATE_TELEGRAM_BOT_TOKEN


bot = telebot.TeleBot(DEBATE_TELEGRAM_BOT_TOKEN)

ts = TopicsService()
ts.update_db()

@bot.message_handler(commands=["help", "start"])
def welcome(message):
    msg = "Hello everyone!"
    bot.reply_to(message, msg)

@bot.message_handler(commands=["get_topic"])
def get_topic(message):
    topic = ts.get_single_topic(is_random=True, language="RU")
    markup = types.InlineKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton("For")
    itembtn2 = types.InlineKeyboardButton("Against")
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, topic, reply_markup=markup)

if __name__ == "__main__":
    # while True:
    #     try:
    #         bot.infinity_polling()
    #     except Exception as e:
    #         print(e)

    bot.infinity_polling() # delete this later


    

