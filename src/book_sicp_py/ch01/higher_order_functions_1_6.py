#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: higher_order_functions_1_6.py
@time: 2020/3/24 10:42
@desc: 1.6 高阶函数
"""
from operator import mul


def square(x):
    return mul(x, x)


def sum_naturals(n):
    """
    计算截至 n 的自然数的和
    :param n:
    :return: sum(n)
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


print("100之内的累加和 =", sum_naturals(100))


def sum_cubes(n):
    """
    计算截至 n 的自然数的立方和
    :param n:
    :return:
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total


print('100之内的立方和 =', sum_cubes(100))


def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / (k * (k + 2)), k + 4
    return total


print('计算pi的近似值 =', pi_sum(100))


# 通用模版
def summation(n, term, next):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), next(k)
    return total


def cube(k):
    return pow(k, 3)


def successor(k):
    return k + 1


def sum_cubes(n):
    return summation(n, cube, successor)


print('3以内的平方和 =', sum_cubes(3))


def identity(k):
    return k


def sum_naturals(n):
    return summation(n, identity, successor)


print('10之内的累加和 =', sum_naturals(10))


def pi_term(k):
    denominator = k * (k + 2)
    return 8 / denominator


def pi_next(k):
    return k + 4


def pi_sum(n):
    return summation(n, pi_term, pi_next)


print('计算pi的近似值 =', pi_sum(1e6))


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


def near(x, f, g):
    """
    测试 f(x) 是否接近于 g(x)
    :param x:
    :param f:
    :param g:
    :return:
    """
    return approx_eq(f(x), g(x))


def approx_eq(x, y, totlerance=1e-5):
    """
    测试相似性，将数值差的绝对值与一个微小的公差值相比
    :param x:
    :param y:
    :param totlerance:
    :return:
    """
    return abs(x - y) < totlerance


def golden_update(guess):
    return 1 / guess + 1


def golden_test(guess):
    return near(guess, square, successor)


print('近似的黄金分割率 =', iter_improve(golden_update, golden_test))

# 测试
phi = 1 / 2 + pow(5, 1 / 2) / 2


def near_test():
    assert near(phi, square, successor), 'phi * phi is not near phi + 1'


def iter_improve_test():
    approx_phi = iter_improve(golden_update, golden_test)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'


# 嵌套定义
def average(x, y):
    return (x + y) / 2


def sqrt_update(guess, x):
    return average(guess, x / guess)


def square_root(x):
    def update(guess):
        return average(guess, x / guess)

    def test(guess):
        return approx_eq(square(guess), x)

    return iter_improve(update, test)


print('采用函数传递计算256的开方计算 =', square_root(256))


def compose1(f, g):
    """
    h(x)=f(g(x))
    :param f:
    :param g:
    :return:
    """

    def h(x):
        return f(g(x))

    return h


add_one_and_square = compose1(square, successor)
print(add_one_and_square(12))


def compose1(f, g):
    return lambda x: f(g(x))


compose1 = lambda f, g: lambda x: f(g(x))


