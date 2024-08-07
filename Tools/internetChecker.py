import socket


# Проверяем наличие интернета
def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80), timeout=1)
        return True
    except OSError:
        return False
