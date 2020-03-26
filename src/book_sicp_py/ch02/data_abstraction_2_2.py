#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: data_abstraction_2_2.py
@time: 2020/3/25 9:03
@desc: 2.2 数据抽象
"""
from operator import getitem


def make_rat(n, d):
    """
    返回分子为n和分母为d的有理数
    :param n:
    :param d:
    :return:
    """
    return (n, d)


def numer(x):
    """
    返回有理数x的分子
    :param x:
    :return:
    """
    return getitem(x, 0)


def denom(x):
    """
    返回有理数x的分母
    :param x:
    :return:
    """
    return getitem(x, 1)


def add_rat(x, y):
    """
    有理数x和y的加法
    :param x:
    :param y:
    :return:
    """
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return make_rat(nx * dy + ny * dy, dx * dy)


def mul_rat(x, y):
    """
    返回有理数x和y的乘法
    :param x:
    :param y:
    :return:
    """
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))


def eq_rat(x, y):
    """
    测试有理数x和y是否相等
    :param x:
    :param y:
    :return:
    """
    return numer(x) * denom(y) == numer(y) * denom(x)


def str_rat(x):
    """
    Return a string 'n/d' for numerator n and denominator d.
    :param x:
    :return:
    """
    return '{0}/{1}'.format(numer(x), denom(x))


half = make_rat(1, 2)
print("1/2的表示形式:", str_rat(half))
third = make_rat(1, 3)
print("1/2*1/3=", str_rat(mul_rat(half, third)))
print("1/2+1/3=", str_rat(add_rat(third, third)))

from math import gcd


def make_rat(n, d):
    g = gcd(n, d)
    return (n // g, d // g)


print("化简：1/2+1/3=", str_rat(add_rat(third, third)))


def make_pair(x, y):
    """Return a function that behaves like a pair."""

    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y

    return dispatch


def getitem_pair(p, i):
    """Return the element at index i of pair p."""
    return p(i)


p = make_pair(1, 2)
print(getitem_pair(p, 0))
print(getitem_pair(p, 1))
