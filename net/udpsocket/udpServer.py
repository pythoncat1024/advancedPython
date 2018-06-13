#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @name   : udpServer.py
# @author : cat
# @date   : 2018/6/13.

import socket
import time


def run_server():
    HOST = ''  # 表示可以绑定任意 ip
    PORT = 26375  # 指定端口
    BUFFER_SIZE = 1024
    ADDR = (HOST, PORT)
    RUNNING_SERVICE = True

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(ADDR)

    while RUNNING_SERVICE:
        print("waiting for message...")
        message, client_addr = server.recvfrom(BUFFER_SIZE)  # 不同于 tcp ，并没有 accept

        msg = "[{}]:{}".format(time.ctime(), str(message, 'utf-8'))
        server.sendto(bytes(msg, 'utf-8'), client_addr)
        print("received from and returned to {addr}".format(addr=client_addr))
    server.close()
    pass


if __name__ == '__main__':
    run_server()
    pass
