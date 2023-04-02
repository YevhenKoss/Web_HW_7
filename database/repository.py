from sqlalchemy import and_
from database.db import session
from database.models import User, Todo


def get_user(login):
    user = session.query(User).filter(User.login == login).first()
    return user


def get_todos(user):
    todos = session.query(Todo).join(User).filter(Todo.user == user).all()
    return todos


def create_todo(title, description, user):
    todo = Todo(title=title, description=description, user=user)
    session.add(todo)
    session.commit()
    session.close()


def update_todo(id_, title, description, user):
    todo = session.query(Todo).filter(and_(Todo.user == user, Todo.id == id_))
    if todo:
        todo.update({"title": title, "description": description})
        session.commit()
        session.close()
        return todo.first()
    return todo


def remove_todo(id_, user):
    r = session.query(Todo).filter(and_(Todo.user == user, Todo.id == id_)).delete()
    session.commit()
    session.close()
    return r
