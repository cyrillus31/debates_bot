from telebot import types


class Poll:
    FOR = "For: %s\n"
    AGAINST = "Against: %s\n"

    def __init__(self, topic: str, proponent: str = "NOBODY YET", opponent: str = "NOBODY YET", language: str = "RU"):
        self.language = language
        self.topic = str(topic) + "\n" + Poll.FOR % proponent + Poll.AGAINST % opponent 
        self.markup = None
        self.proponent = proponent
        self.oppenent = opponent


    def create_markup(self) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton("For", callback_data="for"),
            types.InlineKeyboardButton("Against", callback_data="against"),
            # types.InlineKeyboardButton("Prev", callback_data="something"),
            types.InlineKeyboardButton("Next", callback_data="next"),
            ]
        markup.add(*buttons)
        self.markup = markup
        return self.markup


