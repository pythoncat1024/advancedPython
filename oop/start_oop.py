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
        """
        todo: 注意一点：不一定非要叫 self ; 名称不重要，重要的是位置(第一个参数)
        :param other:
        :return:
        """
        return ThirdClass(self.data + other)

    def __str__(self):
        return "[ThirdClass: {data}]".format(data=self.data)

    def mul(self, other):
        self.data *= other

    def try_some(this):
        pass


class Empty:
    pass


class OneAttr:
    age = 66


class MixedNames:
    data = 'spam'

    def __init__(self, value):
        self.data = value

    def display(self):
        print(self.data, MixedNames.data)


if __name__ == '__main__':
    Empty.name = 'bob'
    x = Empty()
    y = Empty()

    print(Empty.name, x.name, y.name)
    x.name = 'ANN'
    print(Empty.name, x.name, y.name)
    print("================================")

    a = OneAttr()
    b = OneAttr()

    print(OneAttr.age, a.age, b.age)
    a.age += 100
    print(OneAttr.age, a.age, b.age)
    OneAttr.age = 18
    print(OneAttr.age, a.age, b.age)

    print(a.__class__, ThirdClass.__bases__)
    pass

    mn = MixedNames('tom')
    mn.display()
    MixedNames.display(mn)  # 与 mn.display() 等效
