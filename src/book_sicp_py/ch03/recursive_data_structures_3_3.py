#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: recursive_data_structures_3_3.py
@time: 2020/3/27 14:16
@desc: 3.3 递归数据结构
"""
from src.book_sicp_py.ch03.recursive_function_3_2 import square


class Rlist(object):
    """A recursive list consisting of a first element and the rest."""

    class EmptyList(object):
        def __len__(self):
            return 0

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        args = repr(self.first)
        if self.rest is not Rlist.empty:
            args += ', {0}'.format(repr(self.rest))
        return 'Rlist({0})'.format(args)

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]


print("创建列表s[1, 2, 3]")
s = Rlist(1, Rlist(2, Rlist(3)))
print("列表s中从第2个元素开始的序列 =", s.rest)
print("列表s长度 =", len(s))
print("列表s中的第2个元素 =", s[1])


def extend_rlist(s1, s2):
    if s1 is Rlist.empty:
        return s2
    return Rlist(s1.first, extend_rlist(s1.rest, s2))


print("将列表s的rest元素与列表s进行组合 =", extend_rlist(s.rest, s))


def map_rlist(s, fn):
    if s is Rlist.empty:
        return s
    return Rlist(fn(s.first), map_rlist(s.rest, fn))


print("将列表s进行square运算 =", map_rlist(s, square))


def filter_rlist(s, fn):
    if s is Rlist.empty:
        return s
    rest = filter_rlist(s.rest, fn)
    if fn(s.first):
        return Rlist(s.first, rest)
    return rest


print("除去列表s中的偶数 =", filter_rlist(s, lambda x: x % 2 == 1))

print("-----------层次结构-----------")

t = ((1, 2), 3, 4)
big_tree = ((t, t), 5)
print("big_tree =", big_tree)


def map_tree(tree, fn):
    if type(tree) != tuple:
        return fn(tree)
    return tuple(map_tree(branch, fn) for branch in tree)


print("在big_tree上进行square运算 =", map_tree(big_tree, square))


class Tree(object):
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        args = repr(self.entry)
        if self.left or self.right:
            args += ', {0}, {1}'.format(repr(self.left), repr(self.right))
        return 'Tree({0})'.format(args)


def fib_tree(n):
    """
    Return a Tree that represents a recursive Fibonacci calculation.
    Tree 类可以为 fib 的递归实现表示表达式树中计算的值
    """
    if n == 1:
        return Tree(0)
    if n == 2:
        return Tree(1)
    left = fib_tree(n - 2)
    right = fib_tree(n - 1)
    return Tree(left.entry + right.entry, left, right)


print("第5个斐波那契树 =", fib_tree(5))

print("-----------集合-----------")
s = {3, 2, 1, 4, 4}
print("创建s集合 =", s)
print("3是否在s集合中 =", 3 in s)
print("集合s的长度 =", len(s))
print("集合s与{1, 5}的并集 =", s.union({1, 5}))
print("集合s与{6, 5, 4, 3}的交集 =", s.intersection({6, 5, 4, 3}))


def empty(s):
    return s is Rlist.empty


def set_contains(s, v):
    """Return True if and only if set s contains v."""
    if empty(s):
        return False
    elif s.first == v:
        return True
    return set_contains(s.rest, v)


s = Rlist(1, Rlist(2, Rlist(3)))
print("创建集合s =", s)
print("2是否在集合s中 =", set_contains(s, 2))
print("5是否在集合s中 =", set_contains(s, 5))


def adjoin_set(s, v):
    """Return a set containing all elements of s and element v."""
    if set_contains(s, v):
        return s
    return Rlist(v, s)


t = adjoin_set(s, 4)
print("将4加入到集合s中，并命名为集合t =", t)


def intersect_set(set1, set2):
    """Return a set containing all elements common to set1 and set2."""
    return filter_rlist(set1, lambda v: set_contains(set2, v))


print("求集合t 与 集合s进行square运算后的集合 的交集 =", intersect_set(t, map_rlist(s, square)))


def union_set(set1, set2):
    """Return a set containing all elements either in set1 or set2."""
    set1_not_set2 = filter_rlist(set1, lambda v: not set_contains(set2, v))
    return extend_rlist(set1_not_set2, set2)


print("集合s和集合t的并集 =", union_set(t, s))

print("-----------有序集合-----------")


def set_contains(s, v):
    """有序集合的遍历检测"""
    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    return set_contains(s.rest, v)


print("0是否在集合s中 =", set_contains(s, 0))


def intersect_set(set1, set2):
    """有序集合的交集"""
    if empty(set1) or empty(set2):
        return Rlist.empty
    e1, e2 = set1.first, set2.first
    if e1 == e2:
        return Rlist(e1, intersect_set(set1.rest, set2.rest))
    elif e1 < e2:
        return intersect_set(set1.rest, set2)
    elif e2 < e1:
        return intersect_set(set1, set2.rest)


print("集合s和集合s的rest的交集 =", intersect_set(s, s.rest))


def set_contains(s, v):
    if s is None:
        return False
    elif s.entry == v:
        return True
    elif s.entry < v:
        return set_contains(s.right, v)
    elif s.entry > v:
        return set_contains(s.left, v)


def adjoin_set(s, v):
    if s is None:
        return Tree(v)
    if s.entry == v:
        return s
    if s.entry < v:
        return Tree(s.entry, s.left, adjoin_set(s.right, v))
    if s.entry > v:
        return Tree(s.entry, adjoin_set(s.left, v), s.right)


print("通过添加元素的形式构建集合 =", adjoin_set(adjoin_set(adjoin_set(None, 2), 3), 1))

