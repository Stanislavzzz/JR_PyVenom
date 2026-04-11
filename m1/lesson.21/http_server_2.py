import socket


HOST = '127.0.0.1'
PORT = 8081

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f'Сервер запущен на http://{HOST}:{PORT}')

    client_socket, client_address = server_socket.accept()

    with client_socket:
        print(f'Подключение от {client_address}')
        request = client_socket.recv(1024)
        request_text = request.decode('utf-8')
        print(f'Запрос от клиента {client_address}\n{request_text}')

        print('*' * 50)
        request_lines = request_text.split('\r\n')
        print(request_lines)
        request_line = request_lines[0]
        print(f'Первая подстрока {request_line}')
        print('*' * 50)
        method, path, protocol = request_line.split()
        print(f'Метод запроса {method}')
        print(f'Путь запроса  {path}')
        print(f'Версия протокола {protocol}')
        print('*' * 50)


        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "\r\n"
            "<h1>Hello, world!</h1>"
        )
        client_socket.sendall(response.encode())
        print(f'Запрос отправлен {client_address}\n{response}')
