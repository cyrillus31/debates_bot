import re

from telebot import types


class Poll:
    FOR = "For: %s\n"
    AGAINST = "Against: %s\n"
    NOBODY = "NOBODY YET"

    def __init__(self, prev_message: str = "", 
                 topic: str = "", 
                 username: str = "", 
                 user_first_name: str = "", 
                 user_side: str = "", 
                 language: str = "RU",
                ):

        self.language = language
        self.prev_message = prev_message 
        self.topic = topic 
        self.username = f"{user_first_name} ({username})"
        self.user_side = user_side
        self.proponent = "NOBODY YET"
        self.opponent = "NOBODY YET"
        self.error_message = ""

    @staticmethod
    def _parse_prev_message(prev_message: str) -> dict:
        # exp = r"\s*(.+)\s+(?:For: )(.+)\s+(?:Against: )(.+)"
        exp = r"\s*(.+)\s*(?:[For: ]+)(.+)\s+(?:[Against: ]+)(.+)"
        r = re.compile(exp)
        m = r.search(prev_message)
        topic, proponent, opponent = m.groups()
        prev_msg_dict = {
                "topic": topic.strip(), 
                "proponent": proponent.strip(), 
                "opponent": opponent.strip()
                }

        print(prev_msg_dict)

        return prev_msg_dict

    def generate_body(self) -> str:
        if self.prev_message:
            try:
                prev_msg_dict = Poll._parse_prev_message(self.prev_message)
                self.topic = prev_msg_dict["topic"]
                self.proponent = prev_msg_dict["proponent"]
                self.opponent = prev_msg_dict["opponent"]
            except (ValueError, AttributeError) as e:
                self.error_message = f"!! Error: {e} !!"
                

        if self.user_side and self.username:
            if self.user_side == "for":
                self.proponent = self.username
                if self.opponent == self.username:
                    self.opponent = Poll.NOBODY

            elif self.user_side == "against":
                self.opponent = self.username
                if self.proponent == self.username:
                    self.proponent = Poll.NOBODY

        body = f"{self.topic}\n{self.error_message}\nFor : {self.proponent}\nAgainst : {self.opponent}"
        return body

    def generate_markup(self) -> types.InlineKeyboardMarkup:
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton("For", callback_data="for"),
            types.InlineKeyboardButton("Against", callback_data="against"),
            types.InlineKeyboardButton("Re-roll topic", callback_data="reroll"),
            ]
        markup.add(*buttons)
        return markup


