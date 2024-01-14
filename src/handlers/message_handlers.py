from telebot import types

from bot import bot, ts
from polls import Poll


@bot.message_handler(commands=["help", "start"])
def welcome(message):
    msg = "Hello everyone!"
    bot.reply_to(message, msg)

@bot.message_handler(commands=["get_topic"])
def get_topic(message):
    topic = ts.get_single_topic(is_random=True, language="RU").text
    new_poll = Poll(message = topic)
    bot.send_message(message.chat.id, new_poll.generate_body(), reply_markup=new_poll.generate_markup())

