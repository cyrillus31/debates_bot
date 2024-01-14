import re

from telebot import types


class Poll:
    FOR = "For: %s\n"
    AGAINST = "Against: %s\n"
    NOBODY = "NOBODY YET"

    def __init__(self, prev_message: str = "", topic: str = "", username: str = "", user_side: str = "", language: str = "RU"):
        self.language = language
        self.prev_message = prev_message 
        self.topic = topic 
        self.username = username
        self.user_side = user_side
        self.proponent = "NOBODY YET"
        self.opponent = "NOBODY YET"
        self.error_message = ""

    @staticmethod
    def _parse_prev_message(prev_message: str) -> dict:
        # exp = r"\s*(.+)\s+(?:For: )(.+)\s+(?:Against: )(.+)"
        exp = r"\s*(.+)\s*(?:For: )(.+)"
        r = re.compile(exp)
        print(repr(prev_message), "!!!!!!!!!!!!!!!!!!!!!!!")
        print(r.search(repr(prev_message)))
        topic, proponent, opponent = r.search(prev_message).groups()

        return {"topic": topic, "proponent": proponent, "opponent": opponent}

    def generate_body(self) -> str:
        if self.prev_message:
            try:
                prev_msg_dict = Poll._parse_prev_message(self.prev_message)
                self.topic = prev_msg_dict["topic"]
                self.proponent = prev_msg_dict["proponent"]
                self.opponent = prev_msg_dict["opponent"]
            except ValueError as e:
                self.error_message = f"!! Error: {e} !!"

        if self.user_side and self.username:
            if self.user_side == "for":
                self.proponent = self.username
            elif self.user_side == "against":
                self.opponent = self.username

        body = f"{self.topic}\n{self.error_message}\nFor : {self.proponent}\nAgainst : {self.opponent}"
        return body

    def generate_markup(self) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton("For", callback_data="for"),
            types.InlineKeyboardButton("Against", callback_data="against"),
            types.InlineKeyboardButton("Next", callback_data="next"),
            ]
        markup.add(*buttons)
        return markup


