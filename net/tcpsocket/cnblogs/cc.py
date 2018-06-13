#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @name   : cc.py
# @author : cat
# @date   : 2018/6/12.
# @from   : https://www.cnblogs.com/zhangyingai/p/7097922.html
import socket

ip_port = ('127.0.0.1', 8081)
BUFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect_ex(ip_port)  # 拨电话

while True:  # 新增通信循环,客户端可以不断发收消息
    msg = input('>>: ').strip()
    if len(msg) == 0: continue
    s.send(msg.encode('utf-8'))  # 发消息,说话(只能发送字节类型)

    feedback = s.recv(BUFSIZE)  # 收消息,听话
    print(feedback.decode('utf-8'))

s.close()  # 挂电话
