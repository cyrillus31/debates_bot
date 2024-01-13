from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(500), unique=True)
    frequency: Mapped[int] = mapped_column(Integer, default=0)
    language: Mapped[str] = mapped_column(String(3))

    def __repr__(self) -> str:
        return f"{self.text}"

