#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: recursive_function_3_2.py
@time: 2020/3/27 13:26
@desc: 3.2 函数和所生成的过程
"""


def pig_latin(w):
    """
    Return the Pig Latin equivalent of English word w.
    英文单词的 Pig Latin 等价形式将辅音前缀（可能为空）从开头移动到末尾，
    并且添加 -ay 元音
    """
    if starts_with_a_vowel(w):
        return w + 'ay'
    return pig_latin(w[1:] + w[0])


def starts_with_a_vowel(w):
    """Return whether w begins with a vowel."""
    return w[0].lower() in 'aeiou'


print("pun的Pig Latin形式:", pig_latin('pun'))


def fact_iter(n):
    """迭代实现"""
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


print("迭代方式求4的阶乘 =", fact_iter(4))


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print("递归方式求4的阶乘 =", fact(4))


def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)


print("斐波那契序列中的第6个数:", fib(6))


def fib_iter(n):
    prev, curr = 1, 0  # curr is the first Fibonacci number.
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


def memo(f):
    """
    Return a memoized version of single-argument function f.
    通过增加所用空间来减少计算时间
    """
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized


fib = memo(fib)
print("斐波那契序列中的第40个数:", fib(40))

print("---------示例：找零---------")


def count_change(a, kinds=(50, 25, 10, 5, 1)):
    """
    Return the number of ways to change amount a using coin kinds.
    找零方式的总数等于不使用第一种硬币为该金额找零的方式数量，加上使用第一种硬币至少一次的方式数量
    """
    if a == 0:
        return 1
    if a < 0 or len(kinds) == 0:
        return 0
    d = kinds[0]
    return count_change(a, kinds[1:]) + count_change(a - d, kinds)


print("100元的找零方法总数:", count_change(100))

print("---------示例：求幂---------")


def exp(b, n):
    if n == 0:
        return 1
    return b * exp(b, n - 1)

def exp_iter(b, n):
    result = 1
    for _ in range(n):
        result = result * b
    return result

def square(x):
    return x * x

def fast_exp(b, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return square(fast_exp(b, n // 2))
    else:
        return b * fast_exp(b, n - 1)


print("2的100次方 =", fast_exp(2, 100))
