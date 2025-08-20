import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 1. Посмотрим все таблицы в базе
print("=== ВСЕ ТАБЛИЦЫ В БАЗЕ ===")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table in tables:
    print(f"Таблица: {table[0]}")

# 2. Посмотрим структуру таблицы users
print("\n=== СТРУКТУРА ТАБЛИЦЫ users ===")
cursor.execute("PRAGMA table_info(users);")
columns = cursor.fetchall()
for column in columns:
    print(f"Колонка: {column[1]} ({column[2]})")

# 3. Посмотрим данные в таблице users
print("\n=== ДАННЫЕ В ТАБЛИЦЕ users ===")
cursor.execute("SELECT * FROM users;")
users = cursor.fetchall()
if users:
    for user in users:
        print(f"Пользователь: {user}")
else:
    print("В таблице пока нет данных")

# Закрываем соединение
conn.close()