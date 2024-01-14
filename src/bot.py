import telebot

from service import TopicsService
from config import DEBATE_TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(DEBATE_TELEGRAM_BOT_TOKEN)

ts = TopicsService()
ts.update_db()
