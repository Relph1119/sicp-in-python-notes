#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: stream_5_2_5.py
@time: 2020/3/30 16:05
@desc: 5.2.5 流
"""


class Stream(object):
    """A lazily computed recursive list."""

    def __init__(self, first, compute_rest, empty=False):
        self.first = first
        self._compute_rest = compute_rest
        self.empty = empty
        self._rest = None
        self._computed = False

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        assert not self.empty, 'Empty streams have no rest.'
        if not self._computed:
            self._rest = self._compute_rest()
            self._computed = True
        return self._rest

    def __repr__(self):
        if self.empty:
            return '<empty stream>'
        return 'Stream({0}, <compute_rest>)'.format(repr(self.first))


Stream.empty = Stream(None, None, True)


def make_integer_stream(first=1):
    """Return an infinite stream of increasing integers.

    >>> from operator import add
    >>> reduce_stream(add, truncate_stream(make_integer_stream(1), 10), 0)
    55
    """

    def compute_rest():
        return make_integer_stream(first + 1)

    return Stream(first, compute_rest)


s = Stream(1, lambda: Stream(2 + 3, lambda: Stream.empty))
print('创建Stream流 s =', s)

print('s流的第一个元素 =', s.first)
print('s流的第二个元素值 =', s.rest.first)
print('s流的第二个元素对象 =', s.rest)


def map_stream(fn, s):
    if s.empty:
        return s

    def compute_rest():
        return map_stream(fn, s.rest)

    return Stream(fn(s.first), compute_rest)


def filter_stream(fn, s):
    if s.empty:
        return s

    def compute_rest():
        return filter_stream(fn, s.rest)

    if fn(s.first):
        return Stream(s.first, compute_rest)
    return compute_rest()


def truncate_stream(s, k):
    if s.empty or k == 0:
        return Stream.empty

    def compute_rest():
        return truncate_stream(s.rest, k - 1)

    return Stream(s.first, compute_rest)


def stream_to_list(s):
    r = []
    while not s.empty:
        r.append(s.first)
        s = s.rest
    return r


s = make_integer_stream(3)
print('创建Stream流 s =', s)
m = map_stream(lambda x: x * x, s)
print("使用map_stream方法 =", m)
print("将Stream流转换成list =", stream_to_list(truncate_stream(m, 5)))


def primes(pos_stream):
    """
    素数流
    使用埃拉托斯特尼筛法（sieve of Eratosthenes），
    它对整数流进行过滤，移除第一个元素的所有倍数数值。
    :param pos_stream:
    :return:
    """

    def not_divible(x):
        return x % pos_stream.first != 0

    def compute_rest():
        return primes(filter_stream(not_divible, pos_stream.rest))

    return Stream(pos_stream.first, compute_rest)


p1 = primes(make_integer_stream(2))
print(stream_to_list(truncate_stream(p1, 7)))
