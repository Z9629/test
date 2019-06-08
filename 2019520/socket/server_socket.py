# import socket
# #创建实例
# sk = socket.socket()
# #定义绑定IP和端口
# ip_port = ('127.0.0.1',8888)
# #绑定监听
# sk.bind()
# #设置最大监听数
# sk.listen(5)
# #不断循环，接受数据
# while True:
#     #提示信息
#     print("正在等待连接信息...")
#     #接受数据
#     conn,address = sk.accept()
#     #定义信息
#     msg = "Hello Worls!"
#     #返回信息
#     conn.send(msg.encode())
#     #不断接收客户端发来的信息
#     while True:
#
#     #主动关闭连接
#     conn.close()
#
import socket

ip_port = ("127.0.0.1", 8888)

sk = socket.socket() #创建socket实例
sk.bind(ip_port) #绑定IP，端口
sk.listen(5) #监听端口，最大连接数5
print("server is waitting...")
conn,addr = sk.accept() #等待客户端的链接如果没有收到消息就在这里阻塞
while True:
    client_data = str(conn.recv(1024),encoding = "utf8") #接受客户端的信息
    print(client_data)
    conn.sendall(bytes("这是server端的回话",encoding = "utf8"))
conn.close() #断开链接