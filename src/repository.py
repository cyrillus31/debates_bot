from typing import Iterable 

from sqlalchemy import select, func

from database import get_db
from models import Topic


class TopicsRepository:

    def __init__(self):
        pass

    def get(self, offset: int = 0, limit: int = 10000, **kwargs) -> list[Topic | None]:
        with get_db() as db:
            stmt = select(Topic).filter_by(**kwargs).offset(offset).limit(limit)
            results = db.scalars(stmt)
            return [result for result in results] 

    def _add_new_topics_to_db(self, topics_to_add: Iterable[Topic]) -> None:
        only_new_topics = []
        with get_db() as db:
            for topic in topics_to_add:
                if self.get(text=topic.text):
                    continue
                only_new_topics.append(topic)

            db.add_all(only_new_topics)
            db.commit()

    def get_random_multiple(self, amount: int) -> list[Topic]:
        with get_db() as db:
            stmt = select(Topic).order_by(func.random()).limit(amount).all()
            results = db.scalars(stmt)
            return [result for result in results]





