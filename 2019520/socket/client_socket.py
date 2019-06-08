# import socket
# #创建实例,初始化
# client = socket.socket()
# #定义绑定IP和端口
# ip_port = ('127.0.0.1',8888)
# #连接主机
# client.connect(ip_port)
# #接受主机信息
# data = client.recv(1024)
#
# print(data.decode())
#

import socket

ip_port = ("127.0.0.1", 8888)

sk = socket.socket() #创建socket实例
sk.connect(ip_port) #链接服务端
while True:
    user_input = input("请输入:")
    sk.sendall(bytes(user_input,encoding = "utf8")) #向服务端发送信息
    server_reply = sk.recv(1024) #接受服务端的信息
    print(str(server_reply,encoding = "utf8"))
sk.close()
