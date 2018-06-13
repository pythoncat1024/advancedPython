#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @name   : udpClient.py
# @author : cat
# @date   : 2018/6/13.

import socket


def start_client():
    HOST = 'localhost'  # 表示可以绑定任意 ip
    PORT = 26375  # 指定端口
    BUFFER_SIZE = 1024
    ADDR = (HOST, PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        msg = str(input(">: "))
        if not msg:
            break
        client.sendto(bytes(msg, 'utf-8'), ADDR)

        msg, addr = client.recvfrom(BUFFER_SIZE)

        if not msg:
            break
        print(str(msg, 'utf-8'))


if __name__ == '__main__':
    start_client()
    pass
