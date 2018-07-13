#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     iters
   Description : 迭代器对象 __iter__ && __next__
   迭代器提供了一个统一的访问集合的接口。只要是实现了__iter__()或__getitem__()方法的对象，就可以使用迭代器进行访问。
   ==> __iter__() 必须返回一个 实现了 __next__() 方法的对象；
   Author :       cat
   date：          2018/6/29
-------------------------------------------------
   Change Activity:
                   2018/6/29:
-------------------------------------------------
"""


class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        else:
            self.value += 1
            return self.value ** 2


# 多迭代对象
class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


class Iters:
    """
    运算符重载[这里是迭代运算符]是多层级的，只写 __getitem__ 就可以搞定一切，判断 in 默认是走 __contains__ ,不存在，走 __iter__ + __next__
    迭代 默认走 __iter__ + __next__ , 如果不存在，就走 __getitem__

    TODO: 可以通过注释 __contains__ 运行查看效果，注释 __next__ + __iter__ 查看效果
    """

    def __init__(self, value):
        self.data = value

    def __getitem__(self, item):
        print("__getitem__",item , type(item))
        print("get[%s]:" % item, end='')
        return self.data[item]

    # def __iter__(self):
    #     print("iter=> ", end='')
    #     self.ix = 0
    #     return self
    #
    # def __next__(self):
    #     print("next:", end="")
    #     if self.ix == len(self.data): raise StopIteration
    #     item = self.data[self.ix]
    #     self.ix += 1
    #     return item

        # def __contains__(self, item):
        #     print('contains: ', end="")
        #     return item in self.data


if __name__ == "__main__":

    sq = Squares(1, 10)
    for x in sq: print(x, end=' ')
    print()

    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I))

    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')


    class aaa:
        def __iter__(self):
            return BB()

        pass


    class BB:
        def __next__(self):
            return 1


    iter(aaa())

    print("#####################")

    xx = Iters([1, 2, 3, 4, 5])
    print(3 in xx)
    for i in xx: print(i, end="|")
    print()
    print([i ** 2 for i in xx])
    print(list(map(oct, xx)))

    ii = iter(xx)
    while True:
        try:
            print(next(ii), end=" @ ")
        except StopIteration:
            break
