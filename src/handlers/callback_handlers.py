from telebot import types

from bot import bot
from polls import Poll

def callback_data_parser(call: types.CallbackQuery):
    pass

def _edit_poll(**kwargs):
    bot.edit_message_text(**kwargs)

@bot.callback_query_handler(lambda call: call.data in ["for", "against"])
def edit_poll(call: types.CallbackQuery):
    user = call.from_user
    message = call.message
        
    edited_poll = Poll(prev_message=message.text, 
                       username=user.first_name, 
                       user_side=call.data,
                       )

    _edit_poll(text=edited_poll.generate_body(), 
               message_id=message.id, 
               chat_id=message.chat.id,
               reply_markup=edited_poll.generate_markup()
               )


    
    

