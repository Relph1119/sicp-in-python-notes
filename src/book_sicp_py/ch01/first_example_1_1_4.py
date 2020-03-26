#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: first_example_1_1_4.py.py
@time: 2020/3/24 9:34
@desc: 1.1.4 第一个例子
"""

from urllib.request import urlopen

shakespeare = urlopen('http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt')
# 将名称 words 关联到出现在莎士比亚剧本中的所有去重词汇的集合
words = set(shakespeare.read().decode().split())
print(words)

print({w for w in words if len(w) >= 5 and w[::-1] in words})
