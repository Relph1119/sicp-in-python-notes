#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: dict_2_4_5.py
@time: 2020/3/25 16:55
@desc: 2.4.5 字典
"""

numerals = {'I': 1.0, 'V': 5, 'X': 10}
print("字典中的X对应的值:", numerals['X'])

numerals['I'] = 1
numerals['L'] = 50
print(numerals)

print(sum(numerals.values()))

# 通过调用 dict 构造函数，键值对的列表可以转换为字典
print(dict([(3, 9), (4, 16), (5, 25)]))

print("获取字典中A的值:", numerals.get('A', 0))
print("获取字典中V的值:", numerals.get('V', 0))

print({x: x * x for x in range(3, 6)})


def make_dict():
    """Return a functional implementation of a dictionary."""
    records = []

    def getitem(key):
        for k, v in records:
            if k == key:
                return v

    def setitem(key, value):
        for item in records:
            if item[0] == key:
                item[1] = value
                return
        records.append([key, value])

    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
        elif message == 'keys':
            return tuple(k for k, _ in records)
        elif message == 'values':
            return tuple(v for _, v in records)

    return dispatch


d = make_dict()
d('setitem', 3, 9)
d('setitem', 4, 16)
print("获取字典中key=3的值:", d('getitem', 3))
print("获取字典中key=4的值:", d('getitem', 4))
print("获取字典中keys的值:", d('keys'))
print("获取字典中values的值:", d('values'))
