import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, Topic

TOPICS_FOLDER = os.path.join(os.getcwd(), "topics")

engine = create_engine("sqlite:///database.db", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
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
                session.add(new_topic)

    session.commit()




