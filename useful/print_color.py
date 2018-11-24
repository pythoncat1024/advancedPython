#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<a href="https://www.jetbrains.com/help/pycharm/file-template-variables.html">File Template Variables</a>
@project:    advancedPython 
@name:       print_color
@author:     cat
@date:       2018/11/24 23:05       
@product:    PyCharm 
"""
from collections import Iterable


class PrintColor:
    """
    https://www.cnblogs.com/fangbei/p/python-print-color.html
    { 开头部分：\033[显示方式;前景色;背景色m + 结尾部分：\033[0m  }
    注意：开头部分的三个参数：显示方式，前景色，背景色是可选参数，可以只写其中的某一个；
    另外由于表示三个参数不同含义的数值都是唯一的没有重复的，所以三个参数的书写先后顺序没有固定要求，系统都能识别；但是，建议按照默认的格式规范书写。
    对于结尾部分，其实也可以省略，但是为了书写规范，建议\033[***开头，\033[0m结尾。

    -------

    数值表示的参数含义：
    显示方式: 0（默认\）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
    前景色:   30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
    背景色:   40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋 红）、46（青色）、47（白色）
    """

    @staticmethod
    def _color(*args, color='[0;', sep=' , ', end='\n', file=None):
        text = ""
        if not args:
            text = "" + end
        else:
            for obj in args:
                # 可迭代类型进行迭代输出
                if isinstance(obj, Iterable) and not isinstance(obj, str):  # ok
                    ss = "["
                    ee = "]"
                    if isinstance(obj, list):
                        ss = "["
                        ee = "]"
                    elif isinstance(obj, tuple):
                        ss = "("
                        ee = ")"
                    elif isinstance(obj, dict):
                        ss = "{"
                        ee = "}"
                        obj = ["{} : {}".format(k, obj.get(k)) for k in obj]
                    text += "\n" + ss + "\n"
                    for item in obj:
                        text += "\t"
                        text += str(item)
                        text += "\n"
                    if text.endswith("\n"):
                        text = text[0:len(text) - len("\n")]
                    text += "\n"
                    text += ee
                    if len(obj) > 5:
                        text += "\t( SIZE={} )".format(len(obj))
                else:
                    obj = "" if not obj else str(obj)
                    text += obj
                if len(text) > 80:  # 160字符，一行显示不下
                    text += '\n'
                else:
                    text += sep
            if text.endswith(sep):
                text = text[0: - len(sep)]

            while text.endswith("\n"):
                text = text[0:-1]  # 移除多余的换行符
        print('\033{}{}\033[0m'.format(color, text), sep=sep, end=end, file=file)

    @staticmethod
    def green(*args, sep=' , ', end='\n', file=None):
        PrintColor._color(*args, color='[0;32m', sep=sep, end=end, file=file)

    @staticmethod
    def red(*args, sep=' , ', end='\n', file=None):
        PrintColor._color(*args, color='[0;31m', sep=sep, end=end, file=file)

    @staticmethod
    def yellow(*args, sep=' , ', end='\n', file=None):
        PrintColor._color(*args, color='[0;33m', sep=sep, end=end, file=file)

    @staticmethod
    def blue(*args, sep=' , ', end='\n', file=None):
        PrintColor._color(*args, color='[0;34m', sep=sep, end=end, file=file)

    @staticmethod
    def good(*args, sep=' , ', end='\n', file=None):
        PrintColor._color(*args, color='[0;36m', sep=sep, end=end, file=file)

    @staticmethod
    def white(*args, sep=' , ', end='\n', file=None):
        PrintColor._color(*args, color='[0;37m', sep=sep, end=end, file=file)

    @staticmethod
    def normal(*args, sep=' , ', end='\n', file=None):
        PrintColor._color(*args, color='[0;39m', sep=sep, end=end, file=file)

    @staticmethod
    def black(*args, sep=' , ', end='\n', file=None):
        PrintColor._color(*args, color='[0;30m', sep=sep, end=end, file=file)


if __name__ == '__main__':
    PrintColor.red("xxxx", "1234", sep=" ")

    print([1, 2, 3, 4], (1, 2, 3, 4))
    PrintColor.good([1, 2, 3, 4], (1, 2, 3, 4))

    data = {"name": "tom", "password": "xsd23343df13x.as2", "email": "tom@gmail.com"}
    today = [1, 2, 3]
    PrintColor.yellow(data, today, sep=" , ")
