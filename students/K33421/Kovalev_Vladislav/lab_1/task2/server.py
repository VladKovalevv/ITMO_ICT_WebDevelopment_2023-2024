import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.listen(10)
server_socket.settimeout(1)

try:
    while True:
        try:
            client_socket, address = server_socket.accept()
            client_socket.send(
                "Введите через запятую без пробелов значения a и h, "
                "где a - сторона параллелограмма, а h - высота проведенная к стороне a.".encode()
            )

            data = client_socket.recv(1024).decode()
            a, h = (float(num) for num in data.split(","))
            area = a * h

            client_socket.send(f"Площадь параллелограмма: {area}".encode())

        except socket.timeout:
            pass

except KeyboardInterrupt:
    server_socket.close()
