import os

import dotenv

dotenv.load_dotenv()


DEBATE_TELEGRAM_BOT_TOKEN = os.getenv("DEBATE_TELEGRAM_BOT_TOKEN", "")
ADMIN_USER_CHAT_ID = os.getenv("ADMIN_USER_CHAT_ID", "0")


