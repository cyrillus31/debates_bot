from telebot import types, apihelper

from bot import bot, ts
from polls import Poll

def callback_data_parser(call: types.CallbackQuery):
    pass

def _edit_poll(**kwargs):
    try:
        bot.edit_message_text(**kwargs)
    except apihelper.ApiTelegramException as e:
        print("The message was not updated")

@bot.callback_query_handler(lambda call: call.data in ["for", "against"])
def edit_poll(call: types.CallbackQuery):
    user = call.from_user
    message = call.message
        
    edited_poll = Poll(prev_message=message.text, 
                       username=user.username, 
                       user_first_name=user.first_name,
                       user_side=call.data,
                       )
    _edit_poll(text=edited_poll.generate_body(), 
              message_id=message.id, 
              chat_id=message.chat.id,
              reply_markup=edited_poll.generate_markup()
              )

@bot.callback_query_handler(lambda call: call.data == "reroll")
def reroll_poll(call: types.CallbackQuery):
    message = call.message

    for _ in range(10):
        topic = ts.get_single_topic(is_random=True, language="RU").text
        if topic not in message.text:
            break

    new_poll = Poll(topic = topic)

    _edit_poll(text=new_poll.generate_body(),
               message_id=message.id,
               chat_id=message.chat.id,
               reply_markup=new_poll.generate_markup()
               )




    
    

