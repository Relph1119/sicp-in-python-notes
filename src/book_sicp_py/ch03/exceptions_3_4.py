#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: exceptions_3_4.py
@time: 2020/3/27 15:20
@desc: 3.4 异常
"""
from math import sqrt

from src.book_sicp_py.ch01.Newton_method_1_6_6 import newton_update

print("除0运算(x=1/0)")
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print('handling a', type(e))
    x = 0

print("x =", x)


def invert(x):
    result = 1 / x  # Raises a ZeroDivisionError if x is 0
    print('Never printed if x is 0')
    return result


def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)


print("1/2 =", invert_safe(2))
print(invert_safe(0))

print("----------牛顿法的迭代改进----------")


class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess


def iter_improve(update, done, guess=1, max_updates=1000):
    """通过抛出 IterImproveError 异常，储存最新的猜测值来处理任何 ValueError """
    k = 0
    try:
        while not done(guess) and k < max_updates:
            guess = update(guess)
            k = k + 1
        return guess
    except ValueError:
        raise IterImproveError(guess)


def find_root(f, guess=1):
    def done(x):
        return f(x) == 0

    try:
        return iter_improve(newton_update(f), done, guess)
    except IterImproveError as e:
        return e.last_guess


print("使用find_root来寻找2 * x ** 2 + sqrt(x)的零点，该零点是0")
print("求出的零点 =", find_root(lambda x: 2 * x * x + sqrt(x)))
