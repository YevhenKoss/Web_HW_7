from datetime import date, datetime, timedelta
from random import randint, choice

import faker
from sqlalchemy import select

from database.db import session
from database.models import Teacher, Student, Discipline, Grade, Group

'''
Функція отримання списку дат
'''


def date_range(start: date, end: date) -> list:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


'''
Функція створення БД
'''

'''Функція створення фейкових даних та заповнення ними БД'''


def fill_data():
    # Не всі дані будуть динамічними. Створюємо списки предметів та груп
    disciplines = ["Системи тягового електропостачання",
                   "Електропостачання рухомого складу",
                   "Промислове електропостачання",
                   "САПР",
                   "Електропостачання нетягових споживачів",
                   "Системи та мережі",
                   "Тягові підстанції",
                   "Електричні апарати",
                   "Контактна мережа",
                   "Автоматизація систем електропостачання"
                   ]

    groups = ["255", "256", "255M"]

    fake = faker.Faker("uk-UA")
    number_of_teachers = 5
    number_of_students = 50

    def seed_teachers():
        for _ in range(number_of_teachers):
            teacher = Teacher(first_name=fake.first_name(), last_name=fake.last_name())
            session.add(teacher)
        session.commit()

    def seed_disciplines():
        teacher_ids = session.scalars(select(Teacher.id)).all()
        for discipline in disciplines:
            session.add(Discipline(name=discipline, teacher_id=choice(teacher_ids)))
        session.commit()

    def seed_groups():
        for group in groups:
            session.add(Group(name=group))
        session.commit()

    def seed_students():
        group_ids = session.scalars(select(Group.id)).all()
        for _ in range(number_of_students):
            student = Student(first_name=fake.first_name(), last_name=fake.last_name(), group_id=choice(group_ids))
            session.add(student)
        session.commit()

    def seed_grades():
        # дата початку навчання
        start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
        # дата кінця навчання
        end_date = datetime.strptime("2023-06-30", "%Y-%m-%d")
        d_range = date_range(start=start_date, end=end_date)
        discipline_ids = session.scalars(select(Discipline.id)).all()
        student_ids = session.scalars(select(Student.id)).all()

        for d in d_range:
            random_id_discipline = choice(discipline_ids)
            random_ids_student = [choice(student_ids) for _ in range(5)]
            for student_id in random_ids_student:
                grade = Grade(grade=randint(60, 100), date_of=d, student_id=student_id,
                              discipline_id=random_id_discipline)
                session.add(grade)
        session.commit()

    seed_teachers()
    seed_disciplines()
    seed_groups()
    seed_students()
    seed_grades()


if __name__ == '__main__':
    fill_data()
