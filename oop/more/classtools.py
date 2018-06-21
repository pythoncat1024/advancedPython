#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     classtools
   Description :
   Author :       cat
   date：          2018/6/21
-------------------------------------------------
   Change Activity:
                   2018/6/21:
-------------------------------------------------
"""


class AttrDisplay:
    """
    收集自己的全部属性
    """

    def __gatherAttr(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append("{key}={value}".format(key=key, value=getattr(self, key)))
        return ",".join(attrs)

    def __str__(self):
        return "[{} {}]".format(self.__class__.__name__, self.__gatherAttr())
