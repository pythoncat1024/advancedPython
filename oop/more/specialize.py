#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     specialize
   Description :
   Author :       cat
   date：          2018/6/28
-------------------------------------------------
   Change Activity:
                   2018/6/28:
-------------------------------------------------
"""
from abc import ABCMeta, abstractmethod


class Super():
    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()

    def action(self):
        """
        assert 语句 : 如果表达式为假，总是抛出异常
        :return:
        """
        assert False, 'method not implement'


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('in Replacer.method')


class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


class Provider(Super):
    def action(self):
        print('in Provider.action')


if __name__ == "__main__":

    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()

    print('\n Provider')
    x = Provider()
    x.delegate()

    print('xxxxxxxxxxxxxxxxxxxx')
    s = Super()

    s.delegate()
