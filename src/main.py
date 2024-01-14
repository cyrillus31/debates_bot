from bot import bot
import handlers


if __name__ == "__main__":
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(e)

