#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @name   : tcpClient.py
# @author : cat
# @date   : 2018/6/12.

import socket


def open_client():
    HOST = '127.0.0.1'  # 指定服务器 ip
    PORT = 26375  # 指定端口
    BUFFER_SIZE = 1024
    ADDR = (HOST, PORT)
    tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpClientSocket.connect(ADDR)  # 连接服务器

    while True:
        data = str(input("> "))  # 接收键盘输入
        if not data:
            break  # 输入空数据，退出
        tcpClientSocket.send(bytes(data,'utf-8'))  # 将输入发送给服务端
        data = tcpClientSocket.recv(BUFFER_SIZE)  # 接收服务端的返回数据
        if not data:
            break  # 服务端没有返回，退出
        print(str(data,encoding='utf-8'))  # 输出服务端返回的数据
    pass


if __name__ == '__main__':
    open_client()
    pass
