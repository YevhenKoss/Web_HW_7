from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func, event, and_, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(100))
    address = Column(String(150))
    start_work = Column(Date, nullable=False)
    students = relationship("Student", secondary="teachers_to_students", back_populates="teachers")


class Students(Base):
    __tablename__ = "students"
    id = Column("id", Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(100))
    address = Column(String(150))
    teachers = relationship("Teacher", secondary="teachers_to_students", back_populates="students")


class TeacherStudent(Base):
    __tablename__ = "teachers_to_students"
    id = Column("id", Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))


