from telebot import types

from bot import bot, ts
from polls import Poll

GET_MULTIPLE_MESSAGE = "How many topics do you need?"

@bot.message_handler(commands=["help", "start"])
def welcome(message):
    msg = "Hello everyone!"
    bot.reply_to(message, msg)

@bot.message_handler(commands=["get_topic"])
def get_topic(message):
    topic = ts.get_single_topic(is_random=True, language="RU").text
    new_poll = Poll(topic = topic)
    bot.send_message(message.chat.id, new_poll.generate_body(), reply_markup=new_poll.generate_markup())

@bot.message_handler(commands=["get_multiple"])
def get_multiple(message):
    placeholder = "Enter a number from 1 to 30"
    reply = GET_MULTIPLE_MESSAGE
    bot.send_message(message.chat.id, reply, reply_markup=types.ForceReply(input_field_placeholder=placeholder))

@bot.message_handler(func=lambda message: message.reply_to_message.text == GET_MULTIPLE_MESSAGE)
def send_multiple_topcs(message):
    amount = 0
    try:
        amount = int(message.text)
    except ValueError:
        bot.reply_to(message, "This is not a integer number.")
        return

    if not (0 < amount <= 30):
        bot.reply_to(message, "You are asking for an unreasonable amount of topics.")
        return

    for _ in range(0, amount):
        new_topic = ts.get_single_topic(is_random=True)
        new_poll = Poll(topic = new_topic)
        bot.send_message(message.chat.id, new_poll.generate_body(), reply_markup=new_poll.generate_markup())


