#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     privacy
   Description : 模拟实例属性的私有性
   Author :       cat
   date：          2018/6/29
-------------------------------------------------
   Change Activity:
                   2018/6/29:
-------------------------------------------------
"""


class PrivacyException(Exception):
    pass


class Privacy:
    privates = None

    def __setattr__(self, key, value):
        if key in self.privates:
            raise PrivacyException(key, 'not allowed')
        else:
            self.__dict__[key] = value


class Test1(Privacy):
    privates = ['name']


class Test2(Privacy):
    privates = ['name', 'age', 'gender']


if __name__ == "__main__":
    t1 = Test1()

    t1.email = 'py@qq.com'  # ok
    t1.name = 'stone'  # error

    t2 = Test2()
    # print(t2.age)
