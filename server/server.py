import socket
import os
import threading
import queue

# Функция для обработки клиента
def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode('utf-8')  # Максимальное количество данных для приема

        if data:
            if data.startswith("GET /"):
                # Извлекаем запрошенный путь к файлу из запроса
                requested_file = data.split()[1][1:]

                # Получаем содержимое запрошенной страницы
                page_content = get_page_content(requested_file)

                if page_content is not None:
                    # Отправляем содержимое страницы клиенту
                    response = f"HTTP/1.1 200 OK\nContent-Length: {len(page_content)}\n\n".encode('utf-8') + page_content
                else:
                    # Если файл не найден, отправляем ответ "404 Not Found"
                    response = "HTTP/1.1 404 Not Found\n\nFile Not Found".encode('utf-8')
            else:
                # Если запрос не начинается с "GET /", отправляем ответ "400 Bad Request"
                response = "HTTP/1.1 400 Bad Request\n\nBad Request".encode('utf-8')

            # Отправляем ответ клиенту
            client_socket.send(response)
    except Exception as e:
        print(f"Ошибка при обработке клиента: {e}")
    finally:
        client_socket.close()

# Создаем сокет для сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Указываем хост и порт, на котором сервер будет слушать
host = "127.0.0.1"  # Локальный хост (localhost)
port = 12345       # порт

# Привязываем сокет к указанному хосту и порту
server_socket.bind((host, port))

# Начинаем прослушивать входящие соединения
server_socket.listen(5)  # Максимальное количество ожидающих клиентов

print(f"Сервер слушает на {host}:{port}")

def  get_page_content(requested_file):
    # Если путь не указан, используем index.html
    if requested_file == "":
        requested_file = "index.html"

    # Формируем путь к файлу внутри каталога с HTML-страницами
    file_path = os.path.join(os.path.dirname(__file__), "html_pages", requested_file)

    # Проверяем, существует ли запрошенный файл
    if os.path.exists(file_path) and os.path.isfile(file_path):
        # Открываем файл и читаем его содержимое
        with open(file_path, 'rb') as file:
            content = file.read()

        return content
    else:
        return None

# Очередь запросов
request_queue = queue.Queue()

def process_requests():
    while True:
        client_socket, _ = request_queue.get()
        handle_client(client_socket)
        request_queue.task_done()

# Создаем поток для обработки запросов
request_thread = threading.Thread(target=process_requests)
request_thread.start()

while True:
    # Принимаем входящее соединение от клиента
    client_socket, client_address = server_socket.accept()

    print(f"Принято соединение с {client_address}")

    # Добавляем сокет клиента в очередь для обработки
    request_queue.put((client_socket, client_address))
