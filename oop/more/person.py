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


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        pass


if "__main__" == __name__:
    bob = Person('bob')
    tom = Person('tom', pay=66, job='writer')

    print(bob.name, tom.pay)
    pass
