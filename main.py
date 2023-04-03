import argparse

from database.repository import *

parser = argparse.ArgumentParser(description="DB query")
parser.add_argument("--action", help="Command: query_1, query_2, query_3, query_4, query_5, "
                                     "query_6, query_7, query_8, query_9, query_10, query_11, query_12")
parser.add_argument("--disc_id")
parser.add_argument("--group_id")
parser.add_argument("--teach_id")
parser.add_argument("--stud_id")

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get("action")
disc_id = my_arg.get("disc_id")
teach_id = my_arg.get("teach_id")
group_id = my_arg.get("group_id")
stud_id = my_arg.get("stud_id")


def main():
    match action:
        case "query_1":
            print("5 студентів із найбільшим середнім балом з усіх предметів")
            res = query_one()
            for _ in res:
                print(_)
        case "query_2":
            print("Cтудента із найвищим середнім балом з певного предмета")
            print(query_two(disc_id))
        case "query_3":
            print("Cередній бал у групах з певного предмета")
            res = query_three(disc_id)
            for _ in res:
                print(_)
        case "query_4":
            print("Cередній бал на потоці (по всій таблиці оцінок)")
            print(query_four())
        case "query_5":
            print("Kурси, які читає певний викладач")
            res = query_five(teach_id)
            for _ in res:
                print(_)
        case "query_6":
            print("Cписок студентів у певній групі")
            res = query_six(group_id)
            for _ in res:
                print(_)
        case "query_7":
            print("Oцінки студентів у окремій групі з певного предмета")
            res = query_seven(group_id, disc_id)
            for _ in res:
                print(_)
        case "query_8":
            print("Cередній бал, який ставить певний викладач зі своїх предметів")
            res = query_eight(teach_id)
            for _ in res:
                print(_)
        case "query_9":
            print("Cписок курсів, які відвідує певний студент")
            res = query_nine(stud_id)
            for _ in res:
                print(_)
        case "query_10":
            print("Kурси, які певному студенту читає певний викладач")
            res = query_ten(stud_id, teach_id)
            for _ in res:
                print(_)
        case "query_11":
            print("Середній бал, який певний викладач ставить певному студентові")
            print(query_eleven())
        case "query_12":
            print("Оцінки студентів у певній групі з певного предмета на останньому занятті")
            res = query_twelve(disc_id, group_id)
            for _ in res:
                print(_)


if __name__ == '__main__':
    main()
