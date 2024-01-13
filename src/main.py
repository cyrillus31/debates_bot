import telebot

from repository import TopicsRepository


if __name__ == "__main__":
    tr = TopicsRepository()
    tr._add_topics_to_db()
    result = tr.get_topics_in_langugae("RU")
    print(result)

    

