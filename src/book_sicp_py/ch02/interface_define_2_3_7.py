#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: interface_define_2_3_7.py
@time: 2020/3/25 15:47
@desc: 2.3.7 接口约定
"""

# 1.对前 n 个斐波那契数中的偶数求和。
from functools import reduce
from operator import mul

print("-----对前 n 个斐波那契数中的偶数求和------")


def fib(k):
    """Compute the kth Fibonacci number."""
    prev, curr = 1, 0  # curr is the first Fibonacci number.
    for _ in range(k - 1):
        prev, curr = curr, prev + curr
    return curr


def iseven(n):
    return n % 2 == 0


nums = (5, 6, -7, -8, 9)
# filter函数，接受序列，并且返回序列中谓词为真的元素
print("取出序列(5, 6, -7, -8, 9)中的偶数 =", tuple(filter(iseven, nums)))
# map函数，它在序列中的每个元素上调用函数，并且收集结果
print("对序列(5, 6, -7, -8, 9)中的每个元素取绝对值 =", sum(map(abs, nums)))


def sum_even_fibs(n):
    """Sum the first n even Fibonacci numbers."""
    return sum(filter(iseven, map(fib, range(1, n + 1))))


print("对前20个斐波那契数中的偶数求和 =", sum_even_fibs(20))

# 2.列出一个名称中的所有缩写字母，它包含每个大写单词的首字母。
print("-----列出一个名称中的所有缩写字母，它包含每个大写单词的首字母。-----")
print("对Spaces between words进行分割 =", tuple('Spaces between words'.split()))


def first(s):
    return s[0]


def iscap(s):
    """确定一个单词是否大写的谓词"""
    return len(s) > 0 and s[0].isupper()


def acronym(name):
    """Return a tuple of the letters that form the acronym for name."""
    return tuple(map(first, filter(iscap, name.split())))


print("获取University of California Berkeley Undergraduate Graphics Group单词的首字母 =", end='')
print(acronym('University of California Berkeley Undergraduate Graphics Group'))


def acronym(name):
    return tuple(w[0] for w in name.split() if iscap(w))


def sum_even_fibs(n):
    return sum(fib(k) for k in range(1, n + 1) if fib(k) % 2 == 0)


print("-----计算斐波那契数列中奇数的积-----")


def product_even_fibs(n):
    """Return the product of the first n even Fibonacci numbers, except 0."""
    return reduce(mul, filter(iseven, map(fib, range(2, n + 1))))

print("计算前20个斐波那契数列中奇数的积 =", product_even_fibs(20))