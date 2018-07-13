#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     abstruct_class
   Description :
   Author :       cat
   date：          2018/6/28
-------------------------------------------------
   Change Activity:
                   2018/6/28:
-------------------------------------------------
"""
from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    """
    通过注解，让该类不能被直接实例化，必须是继承，然后实例化子类
    """

    @abstractmethod
    def method(self):
        pass


class Sub(Super):
    def method(self):
        print("in Sub.method")


if __name__ == "__main__":
    s = Sub()
    s.method()
    pass
