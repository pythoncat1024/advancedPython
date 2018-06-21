#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     person
   Description :
   Author :       cat
   date：          2018/6/15
-------------------------------------------------
   Change Activity:
                   2018/6/15:
-------------------------------------------------
"""
from oop.more.classtools import AttrDisplay


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        pass


    def giveRaise(self, percent):
        self.pay *= (1 + percent)
        pass


class Manager(Person):
    """
    基于继承的方式去实现
    """

    def __init__(self, name, pay=0):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bounds=0.1):
        # todo: 这里 第三个参数必须提供默认值，否则就不是重载了
        return Person.giveRaise(self, percent + bounds)


class Boss:
    """
    基于组合的实现===> 委托代码模式 [ __attr__ / getattr ]
    """

    def __init__(self, name, pay):
        self.person = Person(name, 'ceo', pay)

    def giveRaise(self, percent, bounds=.3):
        self.person.giveRaise(percent + bounds)

    def __getattr__(self, item):
        return getattr(self.person, item)

    def __str__(self):
        return str(self.person)


class Department:
    """
    聚合 ===> 继承和组合的综合使用
    """

    def __init__(self, *args):
        # print(args) # 得到的是一个 元组
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaise(self, percent):
        """
        todo: 这个有意思了，如果是 Person 就 + 0.1 ，Manager +0.3 ,Boss + 0.4，而且是自动的，这一切是来源于继承，多态
        :param percent: 加钱比例 (0,1)
        :return: NONE
        """
        for person in self.members:
            person.giveRaise(percent)

    def showMembers(self):
        print("==>[")
        for person in self.members:
            print(person)
        print("]")


class A(AttrDisplay):
    def __init__(self):
        self.name = 'Apple'
        self.age = 19


class B(AttrDisplay):
    def __init__(self):
        self.gender = 'female'
        self.friends = ['tom', 'jim', 'candy', 'stone', 'rose']


if __name__ == "__main__":
    bob = Person('bob')
    tom = Person('tom', pay=66, job='writer')

    stone = Manager('stone', 5000)
    print(bob, tom, stone, sep='\n')
    print("------------------------------")
    stone.giveRaise(0.1)
    print(bob, tom, stone, sep='\n')

    print("==============================")

    boss = Boss('victor', 99 + 1)
    print(boss)
    boss.giveRaise(.1)
    print(boss)

    print("++++++++++++++++++++++++++++")
    dep = Department(boss, bob, tom)
    dep.addMember(stone)
    dep.showMembers()
    dep.giveRaise(0.1)
    dep.showMembers()

    print(">>>>>>>>>>>>>>><<<<<<<<<<<<<")

    a = A()
    b = B()

    print(a, b, sep='\n')
    pass
