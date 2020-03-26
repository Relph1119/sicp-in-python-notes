#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: control_1_5.py
@time: 2020/3/24 10:30
@desc: 1.5 控制
"""
from operator import mul


def square(x):
    return mul(x, x)


def print_square(x):
    print(square(x))


def precent_difference(x, y):
    difference = abs(x - y)
    return 100 * difference / x


print('precent_difference(40, 50) =', precent_difference(40, 50))


# 条件语句
def absolute_value(x):
    """Compute abs(x)."""
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x


print('absolute_value(-2) == abs(-2):', absolute_value(-2) == abs(-2))

print('4 < 2:', 4 < 2)
print('5 >= 5:', 5 >= 5)
print('0 == -0:', 0 == -0)

# 三个基本的逻辑运算符
print('True and False:', True and False)
print('True or False:', True or False)
print('not False:', not False)
