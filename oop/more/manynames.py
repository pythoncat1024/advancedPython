#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     manynames
   Description : 5  个 X ， 是完全独立的5个不同变量
   Author :       cat
   date：          2018/6/28
-------------------------------------------------
   Change Activity:
                   2018/6/28:
-------------------------------------------------
"""
X = 11


def f():
    print(X)


def g():
    X = 22
    print(X)


class C:
    x = 33

    def m(self):
        X = 44
        self.X = 55


if __name__ == "__main__":
    pass
