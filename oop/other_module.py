#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     other_module
   Description : 如何引入其他 文件(python 中一个文件就叫一个模块)中内容
   Author :       cat
   date：          2018/6/15
-------------------------------------------------
   Change Activity:
                   2018/6/15:
-------------------------------------------------
"""

from oop.start_oop import FirstClass

if "__main__" == __name__:
    fc = FirstClass()
    fc.set_data(29.8)
    fc.display()

    cc = {1, 2, 3, 4}
    dd = {4, 5, 6, 7}

    print('common:', cc.intersection(dd))
    print('all:', cc+dd)
    pass
