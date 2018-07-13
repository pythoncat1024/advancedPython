#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @name   : change_charset.py
# @author : cat
# @date   : 2018/7/13.
# @desc   : 修改文件编码
# @exec   : python3 charset/change_charset.py ~/Downloads/android架构师/android\ 架构师\ 1-100/

import os
import zipfile
import sys


def get_dir_path():
    cwd = os.getcwd()
    path = cwd[0:cwd.rindex('/')] + "/dir"
    if os.path.exists(path) and os.path.isdir(path):
        return path
    else:
        raise Exception("not found this path")


def un_zip(srcDir, destDir=""):
    if not os.path.isdir(destDir) and os.path.isdir(srcDir):
        destDir = srcDir

    if os.path.isdir(srcDir) and os.path.isdir(destDir):
        'unzip file'
        for file_name in os.listdir(srcDir):
            path = os.path.join(srcDir, file_name)
            if zipfile.is_zipfile(path):
                z = zipfile.ZipFile(path, 'r')
                z.extractall(destDir)
                z.close()
                os.remove(path)
        else:

            print("解压完成，开始转换编码了....")
            'change charset'
            for root_path, dir_names, file_names in os.walk(destDir):
                # print("xx", file_names)
                for fn in file_names:
                    path = os.path.join(root_path, fn)
                    if not zipfile.is_zipfile(path):
                        print("before:", fn)
                        try:
                            fn = fn.encode('cp437').decode('gbk')
                            print("after:", fn)
                            new_path = os.path.join(root_path, fn)
                            os.rename(path, new_path)
                        except Exception as e:
                            print('error:', e)
    else:
        raise Exception("path is not a dir")


def remove_empty(srcDir):
    if os.path.isdir(srcDir):
        for root_path, dir_names, file_names in os.walk(srcDir):
            for dn in dir_names:
                dir_path = os.path.join(root_path, dn)
                if not len(os.listdir(dir_path)):
                    os.rmdir(dir_path)
                    print("rm dir:", dir_path)


if __name__ == '__main__':
    print("input=", sys.argv[1:])
    src = sys.argv[1]
    print("src==>", os.path.isdir(src))
    un_zip(src)
    remove_empty(src)
