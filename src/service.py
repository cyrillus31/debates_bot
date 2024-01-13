import os

from repository import TopicsRepository
from database import Topic


class TopicsService:

    def __init__(self):
        pass

    def _add_topics_to_db(self) -> None:
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
        
    
