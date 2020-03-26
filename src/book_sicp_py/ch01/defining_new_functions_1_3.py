#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: defining_new_functions_1_3.py
@time: 2020/3/24 10:13
@desc: 1.3 定义新函数
"""
from operator import mul, add


def square(x):
    return mul(x, x)


print('sqrt(21) =', square(21))

print('sqrt(2 + 5)=', square(add(2, 5)))

print('sqrt(sqrt(3)) =', square(square(3)))


def sum_squares(x, y):
    """
    计算x和y的平方和
    :param x:
    :param y:
    :return: x*x + y*y
    """
    return add(square(x), square(y))


print('3*3 + 4*4 =', sum_squares(3, 4))
