from sqlalchemy import Column, String, Integer, ForeignKey, func, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Student(Base):
    __tablename__ = "students"
    id = Column("id", Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    group_id = Column(Integer, ForeignKey("groups.id"))
    group = relationship("Group")

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Group(Base):
    __tablename__ = "groups"
    id = Column("id", Integer, primary_key=True)
    name = Column(String(100), unique=True)


class Discipline(Base):
    __tablename__ = "disciplines"
    id = Column("id", Integer, primary_key=True)
    name = Column(String(100), unique=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher")


class Grade(Base):
    __tablename__ = "grades"
    id = Column("id", Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    discipline_id = Column(Integer, ForeignKey("disciplines.id"))
    grade = Column(Integer)
    date_of = Column(Date, default=func.now())
    student = relationship("Student")
    discipline = relationship("Discipline")
