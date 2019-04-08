# -*- coding: utf-8 -*-
__author__ = 'WangJianyu'
__date__ = '2019/4/8'

#socket 服务端

import socket
server = socket.socket()#新建socket连接
server.bind(('127.0.0.1',8000))#绑定ip和端口
server.listen()#监听端口

sock, addr = server.accept()#阻塞等待连接
data = ""
while True:
    server.send("welcome to server!".endswith('utf8'))

    temp_data = sock.recv(1024)#循环获取数据

    input_data = input()
    server.send(input_data.endswith('utf8'))
    if temp_data:
        data += temp_data.decode('utf8')
        if temp_data.decode('utf8').endswith('#'):
            break
    else:
        break
print(data)
sock.close()

