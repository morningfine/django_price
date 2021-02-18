import socket


def http_socket():
    # 创建套接字
    sock = socket.socket()
    # 绑定套接字
    sock.bind(("127.0.0.2", 8001))
    # 设置监听
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        receive = conn.recv(1024)
        print(receive)

        conn.send(b"http/1.1 200 ok\r\nContent-Type:text/html;charset=utf-8\r\n\r\n")
        conn.send('hello,world！'.encode("utf-8"))

        conn.close()


if __name__ == '__main__':
    http_socket()
