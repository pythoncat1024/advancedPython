#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<a href="https://www.jetbrains.com/help/pycharm/file-template-variables.html">File Template Variables</a>
@project:    advancedPython 
@name:       x
@author:     cat
@date:       2018/11/24 18:42       
@product:    PyCharm 
"""
from collections import Iterable


def find_target(folder, ext="torrent", r=True, ):
    """
    :param folder: 指定的目录
    :param r: 是否递归
    :param ext: 扩展名/后缀名
    :return: string 被删除的文件路径集合
    """
    pass

    import os

    exists = os.path.exists(folder)

    if not exists:
        # 路径不存在
        print(folder, "not exists!")
        return None

    # 参数判断完毕：开始遍历的逻辑
    if not ext:
        print("未指定后缀名，不予执行！")
        return None
    file_path_list = []
    if os.path.isfile(folder):  # 如果是文件，而不是目录，直接判断返回结果
        if str(folder).lower().endswith(ext.lower()):
            file_path_list.append(folder)
            return file_path_list

    # 说明一定是目录了，才会走到这一步
    if r:
        # 递归查找
        for dir_path, _useless, file_names in os.walk(folder):
            for name in file_names:
                current_path = os.path.join(dir_path, name)
                # print(current_path)
                if name.lower().endswith(ext.lower()):
                    file_path_list.append(current_path)
    else:
        # 仅在当前目录查找
        dirs = os.listdir(folder)
        for name in dirs:
            current_path = os.path.join(folder, name)
            # print(current_path)
            if os.path.isfile(current_path) and current_path.lower().endswith(ext.lower()):
                # 只保存文件
                file_path_list.append(current_path)

    file_path_list = None if len(file_path_list) == 0 else file_path_list
    return file_path_list


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


def del_target(anything):
    """
    :param anything:  一个文件路径或者一组文件路径
    :return:
    """
    import os
    if not anything: return None

    if isinstance(anything, Iterable):
        for path in anything:
            if os.path.isfile(path):
                os.remove(path)
    else:
        if os.path.isfile(anything):
            os.remove(anything)


def do_exec():
    import sys
    import os
    target_result = ""
    PrintColor.good("input:", str(sys.argv[1:]))
    if len(sys.argv) == 1:
        PrintColor.good("请输入指定文件夹路径以及要批量删除的文件后缀名，并重新执行该程序！!")
    elif len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):
            target_result = find_target(sys.argv[1])
        else:
            PrintColor.red("指定路径不存在，请重新输入！")
    else:
        if len(sys.argv) == 3:
            target_result = find_target(sys.argv[1], sys.argv[2])
        else:
            r = sys.argv[3]
            if str(r).lower() == "false" or str(r).lower() == "0" or str(r).lower() == "no":
                target_result = find_target(sys.argv[1], sys.argv[2], False)
            else:
                target_result = find_target(sys.argv[1], sys.argv[2])
    os.system("clear")
    print("\n======== start ==========")
    PrintColor.good("将要删除的文件:", target_result)
    print("========= end ===========")
    del_target(target_result)


if __name__ == '__main__':
    do_exec()
