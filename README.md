Для розробки створіть "config.ini" з наступним вмістом

[DEV_DB]
USER=postgres
PASSWORD=54321
DB_NAME=web_hw_07
DOMAIN=localhost
PORT=5432



Запити до БД вбудовані в CLI скрипт.
Для запуску команд необхідно ввести в терміналі:

    py main.py --action query_XX

де XX - номер запиту (1 - 12)

В запити №2, 3, 5 - 10, 12 можна вводити додаткові аргументи:

disc_id - id дисципліни;
teach_id - id вчителя;
group_id - id групи;
stud_id - id студента;

Якщо додаткові аргументи не ввести, відповідному аргументу буде присвоїне значення за замовчуванням.
Для всіх додаткових аргументів, значення за замовчуванням = 1.

Файл repository.py містить код запитів.

Прриклади команд для запитів:

№1

    py main.py --action query_1

№2

    py main.py --action query_2 --disc_id 1

№3

    py main.py --action query_3 --disc_id 1

№4

    py main.py --action query_4

№5

    py main.py --action query_5 --teach_id 1

№6

    py main.py --action query_6 --group_id 1

№7

    py main.py --action query_7 --group_id 1 --disc_id 1

№8

    py main.py --action query_8 --teach_id 1

№9

    py main.py --action query_9 --stud_id 1

№10

    py main.py --action query_10 --stud_id 1 --teach_id 1

№11

    py main.py --action query_11

№12

    py main.py --action query_12 --disc_id 1 --group_id 1

