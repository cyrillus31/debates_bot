import telebot

from service import TopicsService
from config import DEBATE_TELEGRAM_BOT_TOKEN


bot = telebot.TeleBot(DEBATE_TELEGRAM_BOT_TOKEN)
print(DEBATE_TELEGRAM_BOT_TOKEN)
print(bot)


@bot.message_handler(commands=["help", "start"])
def welcome(message):
    msg = "Hello everyone!"
    bot.reply_to(message, msg)


if __name__ == "__main__":
    topics_service = TopicsService()
    topics_service.add_new_topics_to_db()
    bot.infinity_polling()


    

