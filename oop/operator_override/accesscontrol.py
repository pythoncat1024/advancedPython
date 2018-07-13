#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     accesscontrol
   Description : __getattr__ , __setattr__
   Author :       cat
   date：          2018/6/29
-------------------------------------------------
   Change Activity:
                   2018/6/29:
-------------------------------------------------
"""


class AccessControl:
    """
    对不存在的属性的控制
    """

    def __getattr__(self, item):
        if item == "age":
            return 40
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        if key == "age":
            self.__dict__[key] = value
            # self.key = value  ==> TODO: 递归调用导致栈溢出异常
        else:
            raise AttributeError


if __name__ == "__main__":
    ac = AccessControl()
    print(ac.age)
    ac.age = 99
    print(ac.age)
    ac.name = 55 # exception
    pass
