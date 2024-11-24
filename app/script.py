import os

# Получаем переменную окружения
username = os.getenv("username", "default_user")  # "default_user" на случай, если переменная не задана

# Выводим секрет в консоль
print(f"А вот и твой секрет: {username}")
