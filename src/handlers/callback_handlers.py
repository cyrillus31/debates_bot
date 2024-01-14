from telebot import types

from bot import bot
from polls import Poll

def callback_data_parser(call: types.CallbackQuery):
    pass

def _edit_poll(**kwargs):
    bot.edit_message_text(**kwargs)

@bot.callback_query_handler(lambda call: call.data == "for")
def register_vote(call: types.CallbackQuery):
    user = call.from_user
    message = call.message
    topic = message.text.split("\n")[0]
    edited_poll = Poll(topic=topic, proponent=user.first_name)
    _edit_poll(text=edited_poll.topic, 
               message_id=message.id, 
               chat_id=message.chat.id,
               reply_markup=edited_poll.create_markup()
               )


    
    

