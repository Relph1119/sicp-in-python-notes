#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Newton_method_1_6_6.py
@time: 2020/3/24 11:19
@desc: 1.6.6 示例：牛顿法
"""
from operator import mul


def square(x):
    return mul(x, x)


def square_root(a):
    return find_root(lambda x: square(x) - a)


def logarithm(a, base=2):
    return find_root(lambda x: pow(base, x) - a)


def approx_derivative(f, x, delta=1e-5):
    """
    计算f(x)的斜率
    :param f:
    :param x:
    :param delta:
    :return:
    """
    df = f(x + delta) - f(x)
    return df / delta


def newton_update(f):
    """
    计算f(x)的导数
    :param f:
    :return:
    """

    def update(x):
        return x - f(x) / approx_derivative(f, x)

    return update


def approx_eq(x, y, totlerance=1e-5):
    """
    测试相似性，将数值差的绝对值与一个微小的公差值相比
    :param x:
    :param y:
    :param totlerance:
    :return:
    """
    return abs(x - y) < totlerance


# 作为一般方法的函数
def iter_improve(update, test, guess=1):
    """
    实现了迭代改进的一般方法，并且可以用于计算黄金比例
    :param update:
    :param test:
    :param guess:
    :return:
    """
    while not test(guess):
        guess = update(guess)
    return guess


def find_root(f, initial_guess=10):
    def test(x):
        return approx_eq(f(x), 0)

    return iter_improve(newton_update(f), test, initial_guess)


print('计算16的开方 =', square_root(16))

print('计算32的2次方根 =', logarithm(32, 2))
