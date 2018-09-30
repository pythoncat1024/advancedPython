#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     call_super_init
   Description :
   Author :       cat
   date：          2018/6/28
-------------------------------------------------
   Change Activity:
                   2018/6/28:
-------------------------------------------------
"""


class Origin:
    def __init__(self):
        self.name = 'origin'
        print(self.name)


class Sub(Origin):
    def __init__(self):
        super().__init__()
        # Origin.__init__(self) # 与 super().__init__() 等效
        print(super(), "###", super)


if __name__ == "__main__":
    s = Sub()
    pass
