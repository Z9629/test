# import socket
# sock = socket.socket()
# sock.bind(('127.0.0.1',8080))
# sock.listen(5)
# while True:
#     conn,addr = sock.accept()
#     data = conn.recv(8096)
#     conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
#     conn.send(b'123123')
#     conn.close()

#------------------------


import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8080))
sock.listen(5)

while True:
    conn, addr = sock.accept()  # hang住
    # 有人来连接了
    # 获取用户发送的数据
    data = conn.recv(8096)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    conn.send(b'123123')
    conn.close()