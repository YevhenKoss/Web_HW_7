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

Файл repository.py містить код запитів.