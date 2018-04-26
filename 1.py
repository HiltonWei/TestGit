#!/usr/bin/env python
# coding=utf-8
import os
# from fabric.colors import *
'''
功能：在文件夹中查找某一文件，找到后返回True与文件所在目录路径。
参数：filepath, 要查找的目录
参数：filename, 要查找的文件
扩展1：find_depth, 查找时指定递归深度；
扩展2：ignore_path, 查找时忽略某些目录；
'''

def find_file(self, filepath, filename, find_depth=1, ignore_path=['.git', 'node_modules']):
    """查找文件"""
    # print blue("当前查找目录：{}，递归层级：{}".format(filepath, find_depth))
    # 递归深度控制
    find_depth -= 1
    for file_ in os.listdir(filepath):
        # print cyan("file: {}".format(file_))
        if isfile(join(filepath, file_)):
            # print "当前文件：{}".format(file_)
            if file_ == filename:
                return True, filepath
        elif find_depth <= 0:  # 递归深度控制, 为0时退出
            # print yellow("超出递归深度，忽略!")
            continue
        elif file_ in ignore_path:  # 忽略指定目录
            # print yellow("此目录在忽略列表中，跳过！")
            continue
        else:
            result, abs_path = self.find_file(filepath=join(filepath, file_),
                                              filename=filename,
                                              find_depth=find_depth)
            if result:
                print green("找到{}文件，所在路径{}".format(filename, abs_path))
                return result, abs_path
    return False, filepath

result, filepath = find_build(filepath="/data/deploy/jenkins/data/jobs/sit-zjims-mobile/workspace/", filename="gulpfile.js", find_depth=3)