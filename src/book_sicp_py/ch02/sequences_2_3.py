#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: sequences_2_3.py
@time: 2020/3/25 9:36
@desc: 2.3 序列
"""

# rlist：递归列表
empty_rlist = None


def make_rlist(first, rest):
    """Make a recursive list from its first element and the rest."""
    return (first, rest)


def first(s):
    """Return the first element of a recursive list s."""
    return s[0]


def rest(s):
    """Return the rest of the elements of a recursive list s."""
    return s[1]


print("-----递归列表-----")
counts = make_rlist(1, make_rlist(2, make_rlist(3, make_rlist(4, empty_rlist))))
print("序列的第1个元素 =", first(counts))
print("序列余下的元素 =", rest(counts))


def len_rlist(s):
    """Return the length of recursive list s."""
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length


def getitem_rlist(s, i):
    """Return the element at index i of recursive list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


print("序列的长度 =", len_rlist(counts))
print("序列的第二个元素 =", getitem_rlist(counts, 1))

print("-----元组-----")
digits = (1, 8, 2, 8)
print("序列digits(1, 8, 2, 8)的长度 =", len(digits))
print("序列digits的第四个元素 =", digits[3])
print((2, 7) + digits * 2)

alternates = (-1, 2, -3, 4, -5)
print("对序列(-1, 2, -3, 4, -5)进行取绝对值 =", tuple(map(abs, alternates)))

print("-----序列迭代-----")


def count(s, value):
    """Count the number of occurrences of value in sequence s."""
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total


print("计算8在digits序列中出现的次数 =", count(digits, 8))


def count(s, value):
    """Count the number of occurrences of value in sequence s."""
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total


print("计算8在digits序列中出现的次数 =", count(digits, 8))
