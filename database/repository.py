from sqlalchemy import func, desc, and_, select

from database.db import session
from database.models import Student, Discipline, Grade, Group, Teacher


def query_one():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    # SELECT s.fullname, ROUND(AVG(g.grade), 3) AS avg_grade
    # FROM grades g
    # LEFT JOIN students s ON s.id = g.student_id
    # GROUP BY s.id
    # ORDER BY avg_grade DESC
    # LIMIT 5;
    result = session.query(Student.fullname,
                           func.round(func.avg(Grade.grade),
                                      2).label("avg_grade")) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc("avg_grade")).limit(5).all()
    # order_by(Grade.grade.desc())
    return result


def query_two(disc_id):
    # Знайти студента із найвищим середнім балом з певного предмета
    # SELECT d.name, s.fullname, ROUND(AVG(g.grade), 3) AS avg_grade
    # FROM grades g
    # LEFT JOIN students s ON s.id = g.student_id
    # LEFT JOIN disciplines d ON d.id = g.discipline_id
    # WHERE d.id = 1
    # GROUP BY s.id, d.id
    # ORDER BY avg_grade DESC
    # LIMIT 1;
    if not disc_id:
        disc_id = 1
    result = session.query(Discipline.name,
                           Student.fullname,
                           func.round(func.avg(Grade.grade), 2).label("avg_grade")) \
        .select_from(Grade).join(Student).join(Discipline) \
        .filter(Discipline.id == disc_id) \
        .group_by(Student.id, Discipline.name).order_by(desc("avg_grade")).limit(1).first()
    return result


def query_three(disc_id):
    # Знайти середній бал у групах з певного предмета
    # SELECT gr.name, d.name, ROUND(AVG(g.grade), 3) AS avg_grade
    # FROM grades g
    # LEFT JOIN students s ON s.id = g.student_id
    # LEFT JOIN disciplines d ON d.id = g.discipline_id
    # LEFT JOIN [groups] gr ON gr.id = s.group_id
    # WHERE d.id = 1
    # GROUP BY gr.id, d.id
    # ORDER BY avg_grade DESC;
    if not disc_id:
        disc_id = 1
    result = session.query(Group.name, Discipline.name, func.round(func.avg(Grade.grade), 2).label("avg_grade")) \
        .select_from(Grade).join(Student).join(Discipline).join(Group).filter(Discipline.id == disc_id) \
        .group_by(Group.id, Discipline.name).order_by(desc("avg_grade")).all()
    return result


def query_four():
    # Знайти середній бал на потоці (по всій таблиці оцінок)
    # SELECT ROUND(AVG(g.grade), 3) AS avg_grade
    # FROM grades g;
    result = session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade")) \
        .select_from(Grade).first()
    return result


def query_five(teach_id):
    # Знайти які курси читає певний викладач
    # SELECT t.fullname, d.name
    # FROM disciplines d
    # LEFT JOIN teachers t ON t.id = d.teacher_id
    # WHERE t.id = 5
    # ORDER BY d.id;
    if not teach_id:
        teach_id = 1
    result = session.query(Teacher.fullname, Discipline.name).select_from(Discipline).join(Teacher) \
        .filter(Teacher.id == teach_id).order_by(Discipline.id).all()
    return result


def query_six(group_id):
    # Знайти список студентів у певній групі
    # SELECT s.fullname, g.name
    # FROM students s
    # LEFT JOIN groups g ON g.id = s.group_id
    # WHERE g.id = 3
    # ORDER BY s.fullname;
    if not group_id:
        group_id = 1
    result = session.query(Student.fullname, Group.name).select_from(Student).join(Group) \
        .filter(Group.id == group_id).order_by(Student.fullname).all()
    return result


def query_seven(group_id, disc_id):
    # Знайти оцінки студентів у окремій групі з певного предмета
    # SELECT gr.name, s.fullname,  d.name, g.grade
    # FROM grades g
    # LEFT JOIN students s ON s.id = g.student_id
    # LEFT JOIN disciplines d ON d.id = g.discipline_id
    # LEFT JOIN [groups] gr ON gr.id = s.group_id
    # WHERE d.id = 10 AND gr.id = 1
    # ORDER BY s.fullname;
    if not group_id:
        group_id = 1
    if not disc_id:
        disc_id = 1
    result = session.query(Group.name, Student.fullname, Discipline.name, Grade.grade).select_from(Grade) \
        .join(Student).join(Discipline).join(Group).filter(and_(Group.id == group_id, Discipline.id == disc_id)) \
        .order_by(Student.fullname).all()
    return result


def query_eight(teach_id):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів
    # SELECT t.fullname, d.name, ROUND(AVG(g.grade), 3) AS avg_grade
    # FROM grades g
    # LEFT JOIN disciplines d ON d.id = g.discipline_id
    # LEFT JOIN teachers t ON t.id = d.teacher_id
    # WHERE t.id = 5
    # GROUP BY d.id
    # ORDER BY avg_grade DESC;
    if not teach_id:
        teach_id = 1
    result = session.query(Teacher.fullname, Discipline.name, func.round(func.avg(Grade.grade), 3).label("avg_grade")) \
        .select_from(Grade).join(Discipline).join(Teacher).filter(Teacher.id == teach_id).group_by(Teacher.fullname,
                                                                                            Discipline.name) \
        .order_by(desc("avg_grade")).all()
    return result


def query_nine(stud_id):
    # Знайти список курсів, які відвідує певний студент
    # SELECT s.fullname, d.name
    # FROM grades g
    # LEFT JOIN students s ON s.id = g.student_id
    # LEFT JOIN disciplines d ON d.id = g.discipline_id
    # WHERE s.id = 50
    # GROUP BY d.id
    if not stud_id:
        stud_id = 1
    result = session.query(Student.fullname, Discipline.name).select_from(Grade).join(Discipline).join(Student) \
        .filter(Student.id == stud_id).group_by(Discipline.name, Student.fullname).all()
    return result


def query_ten(stud_id, teach_id):
    # Список курсів, які певному студенту читає певний викладач
    # SELECT s.fullname, d.name, t.fullname
    # FROM grades g
    # LEFT JOIN students s ON s.id = g.student_id
    # LEFT JOIN disciplines d ON d.id = g.discipline_id
    # LEFT JOIN teachers t ON t.id = d.teacher_id
    # WHERE s.id = 1 AND t.id = 1
    # GROUP BY d.id
    if not stud_id:
        stud_id = 1
    if not teach_id:
        teach_id = 1
    result = session.query(Student.fullname, Discipline.name, Teacher.fullname).select_from(Grade).join(Discipline) \
        .join(Student).join(Teacher).filter(and_(Student.id == stud_id, Teacher.id == teach_id)) \
        .group_by(Discipline.name, Teacher.fullname, Student.fullname).all()
    return result


def query_eleven():
    return "Не зробив :)"


def query_twelve(disc_id, group_id):
    # Оцінки студентів у певній групі з певного предмета на останньому занятті.
    # select s.id, s.fullname, g.grade, g.date_of
    # from grades g
    # join students s on s.id = g.student_id
    # where g.discipline_id = 3 and s.group_id = 3 and g.date_of = (
    #     select max(date_of)
    #     from grades g2
    #     join students s2 on s2.id = g2.student_id
    #     where g2.discipline_id = 3 and s2.group_id = 3);
    if not group_id:
        group_id = 1
    if not disc_id:
        disc_id = 1
    subquery = (select(func.max(Grade.date_of)).join(Student).filter(and_(Grade.discipline_id == disc_id,
                                                                          Student.group_id == group_id)).scalar_subquery())

    result = session.query(Student.id, Student.fullname, Grade.grade, Grade.date_of) \
        .select_from(Grade) \
        .join(Student) \
        .filter(and_(Grade.discipline_id == disc_id, Student.group_id == group_id, Grade.date_of == subquery)).all()
    return result
