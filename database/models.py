from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, declarative_base

from database.db import engine

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(String(50), unique=True)
    password = Column(String(50))


class Todo(Base):
    __tablename__ = "todos"
    id = Column("id", Integer, primary_key=True)
    title = Column("title", String(150), nullable=False, index=True)
    description = Column("description", String(300), nullable=False, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    user_id = Column("user_id", Integer, ForeignKey("users_id"))
    user = relationship("User")


Base.metadata.create_all(engine)
