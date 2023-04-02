import argparse

from database.repository import *

parser = argparse.ArgumentParser(description="DB query")
parser.add_argument("--action", help="Command: query_1, query_2, query_3, query_4, query_5, "
                                     "query_6, query_7, query_8, query_9, query_10, query_12")


arguments = parser.parse_args()
my_arg = vars(arguments)
action = my_arg.get("action")


def main():
    match action:
        case "query_1":
            res = query_one()
            for _ in res:
                print(_)
        case "query_2":
            print(query_two())
        case "query_3":
            res = query_three()
            for _ in res:
                print(_)
        case "query_4":
            print(query_four())
        case "query_5":
            res = query_five()
            for _ in res:
                print(_)
        case "query_6":
            res = query_six()
            for _ in res:
                print(_)
        case "query_7":
            res = query_seven()
            for _ in res:
                print(_)
        case "query_8":
            res = query_eight()
            for _ in res:
                print(_)
        case "query_9":
            res = query_nine()
            for _ in res:
                print(_)
        case "query_10":
            res = query_ten()
            for _ in res:
                print(_)
        case "query_12":
            res = query_twelve()
            for _ in res:
                print(_)


if __name__ == '__main__':
    main()
