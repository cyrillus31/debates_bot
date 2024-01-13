import os
from typing import Iterable 

from sqlalchemy import ScalarResult, select
import sqlite3

from config import TOPICS_FOLDER
from database import get_db
from models import Topic


class TopicsRepository:

    def __init__(self):
        pass

    def get_topics_in_langugae(self, language: str = "RU") -> list[Topic]:
        with get_db() as db:
            stmt = select(Topic).where(Topic.language.__eq__(language))
            results = db.scalars(stmt)
            return [result for result in results]

    def _get_by_text(self, text: str) -> Topic | None:
        with get_db() as db:
            stmt = select(Topic).where(Topic.text.like(text))
            result = db.scalars(stmt).one()
            return result

    def _add_topics_to_db(self, topics: Iterable[Topic]) -> None:
        new_topics = []
        with get_db() as db:
            for topic in topics:
                if self._get_by_text(text=topic.text):
                    continue
                new_topics.append(topic)

            db.add_all(new_topics)
            db.commit()
            




