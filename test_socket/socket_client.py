# -*- coding: utf-8 -*-
__author__ = 'WangJianyu'
__date__ = '2019/4/8'

import socket
client = socket.socket()
client.connect(('127.0.0.1',8000))


#接收用户数据：
while True:
    input_data = input()
# client.send(b"wangjianyu")
    client.send(input_data.encode("utf-8"))
    server_data = client.recv(1024)
    print('server response: {}'.format(server_data.decode('utf8')))


# client.close()