#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     start_oop
   Description :
   Author :       cat
   date：          2018/6/15
-------------------------------------------------
   Change Activity:
                   2018/6/15:
-------------------------------------------------
"""


class FirstClass:
    def set_data(self, data):
        self.data = data

    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print("Current value {data}".format(data=self.data))


class ThirdClass(SecondClass):
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return "[ThirdClass: {data}]".format(data=self.data)

    def mul(self, other):
        self.data *= other


if "__main__" == __name__:
    pass
