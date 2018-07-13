#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     numbers
   Description :
   Author :       cat
   date：          2018/6/28
-------------------------------------------------
   Change Activity:
                   2018/6/28:
-------------------------------------------------
"""


class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        '- 运算符重载'
        return Number(self.data - other)


class Indexer:
    def __getitem__(self, item):
        """
        获取 instance[i] 需要重新的方法;
        索引迭代 for x in obj 也是调用该方法
        """
        return item ** 2


class Totoro:
    data = [2, 3, 4, 5, 6, 7]

    def __getitem__(self, item):
        "todo: 这里的 item 并不是数字，而是 一个 slice(2,4,None) 的 对象"
        print("totoro:", item)  # totoro: slice(2, 4, None)
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value


class ForLoop:
    def __getitem__(self, item):
        return self.data[item]


if __name__ == "__main__":
    ff = ForLoop()
    ff.data = "spam"
    for item in ff: print(item, end=' ')
    print()
    n = Number(5)
    print((n - 2).data)  # 3
    pass

    idx = Indexer()
    for x in range(0, 12): print(x, '\t-->\t', idx[x])

    print("Totoro", Totoro()[2:4])

    print(type(slice(2, 4, None)))  # slice
    tt = Totoro()
    tt[5] = 13
    print(tt[3:6])

    print(list(tt),tuple(tt),5 in tt ) # 这些操作能做，全是因为 实现了 __getitem__()
