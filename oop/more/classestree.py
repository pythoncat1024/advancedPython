#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     classestree
   Description : 教你爬树
   Author :       cat
   date：          2018/6/28
-------------------------------------------------
   Change Activity:
                   2018/6/28:
-------------------------------------------------
"""


def classtree(cls, indent):
    print("." * indent + cls.__name__)
    for sub in cls.__bases__:
        classtree(sub, indent + 3)


def instancetree(inst):
    print("Tree of inst %s" % inst)
    classtree(inst.__class__,3)


if __name__ == "__main__":
    class A: pass


    class B(A): pass


    class C(A): pass


    class D(B, C): pass


    class E: pass


    class F(D, E): pass


    instancetree(F())

    pass
