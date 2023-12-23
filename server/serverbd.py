import mysql.connector

# Параметры подключения к базе данных
host = '127.0.0.1'
user = 'your_database_user'
password = 'your_database_password'
database = 'GRADUATE QUALIFYING WORK'

# Подключение к базе данных
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Создание курсора для выполнения SQL-запросов
cursor = connection.cursor()

# Пример выполнения SQL-запроса (замените на свой код)
cursor.execute("SELECT * FROM your_table_name")

# Получение результатов запроса
results = cursor.fetchall()

# Закрытие курсора и соединения
cursor.close()
connection.close()
