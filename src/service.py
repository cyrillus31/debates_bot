import os
import random

from repository import TopicsRepository
from database import Topic

from config import TOPICS_FOLDER


class TopicsService:

    def __init__(self):
        self.repository = TopicsRepository()

    def _add_new_topics_to_db(self) -> None:
        topics_to_add = []
        root, folders, files = next(os.walk(TOPICS_FOLDER))

        for file in files:
            file = os.path.join(root, file)
            basename = os.path.basename(file)
            language, extension = os.path.splitext(basename)

            if extension != ".txt":
                continue

            with open(file, "r", encoding="utf-8") as txtfile:
                for line in txtfile:
                    new_topic = Topic(text=line, language=language)
                    topics_to_add.append(new_topic)

        self.repository._add_new_topics_to_db(topics_to_add)

    def update_db(self) -> None:
        self._add_new_topics_to_db()

    def get_topics(self, amount: int) -> list[Topic]:
        topics = self.repository.get_random_multiple(amount)
        return topics

    def get_single_topic(self, is_random=True, **kwargs) -> Topic | None:
        topics = self.repository.get(**kwargs)
        if not is_random:
            return topics[0]
        amount_of_topics = len(topics) 
        random_index = random.randint(0, amount_of_topics-1)
        return topics[random_index]

        
    
