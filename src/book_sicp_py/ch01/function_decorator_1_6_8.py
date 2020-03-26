#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: function_decorator_1_6_8.py
@time: 2020/3/24 13:35
@desc: 1.6.8 函数装饰器
"""


def trace1(fn):
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)

    return wrapped


@trace1
def triple(x):
    return 3 * x


print(triple(12))
