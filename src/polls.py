from telebot import types


class Poll:
    FOR = "For: %s\n"
    AGAINST = "Against: %s\n"
    NOBODY = "NOBODY YET"

    def __init__(self, message: str, username: str = "", user_side: str = "", language: str = "RU"):
        self.language = language
        self.message = message 

    def generate_body(self):
        msg = self.message.split("\n")
        topic = msg[0]
        proponent = msg[-2]
        opponent = msg[-1]
        return str((topic, proponent, opponent))

    def generate_markup(self) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton("For", callback_data="for"),
            types.InlineKeyboardButton("Against", callback_data="against"),
            types.InlineKeyboardButton("Next", callback_data="next"),
            ]
        markup.add(*buttons)
        return markup


