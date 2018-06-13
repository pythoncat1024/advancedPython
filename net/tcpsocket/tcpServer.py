#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @name   : tcpServer.py
# @author : cat
# @date   : 2018/6/12.

import socket
import time


def run_service():
    """
    "时间服务器"：返回客户端发送过来的数据，以及服务器当前的时间
    :return: none
    """
    HOST = ''  # 表示可以绑定任意 ip
    PORT = 26375  # 指定端口
    BUFFER_SIZE = 1024
    ADDR = (HOST, PORT)
    RUNNING_SERVICE = True
    tcpService = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpService.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 加入一条socket配置，重用ip和端口#加入
    tcpService.bind(ADDR)
    tcpService.listen(5)  # 最大同时连接数

    while RUNNING_SERVICE:
        print("waiting for connection...")
        tcpClient, clientAddr = tcpService.accept()
        print("connected from {}".format(clientAddr))

        while True:
            data = tcpClient.recv(BUFFER_SIZE)  # data --> bytes 字节数组
            # print("data=====", data)
            if not data:
                break
            timeString = "[{}] {}".format(time.ctime(), str(data, encoding='utf-8'))

            # print('ts===', timeString) --> 将要返回给客户端的内容
            tcpClient.send(bytes(timeString, 'utf-8'))
        tcpClient.close()  # 一次与客户端的交互完成。
    tcpService.close()
    pass


if __name__ == '__main__':
    run_service()
    pass
