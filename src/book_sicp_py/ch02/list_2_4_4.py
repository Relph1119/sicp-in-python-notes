#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: list_2_4_4.py
@time: 2020/3/25 16:27
@desc: 2.4.4 列表
"""

from unicodedata import lookup

from src.book_sicp_py.ch02.sequences_2_3 import empty_rlist, len_rlist, getitem_rlist, make_rlist, first, rest

# 扑克牌发明于中国，大概在 9 世纪。早期的牌组中有三个花色，它们对应钱的三个面额
# A list literal
chinese_suits = ['coin', 'string', 'myriad']
print("中国的牌组:", chinese_suits)
# Two names refer to the same list
suits = chinese_suits

# 扑克牌传到欧洲（也可能通过埃及） 之后，西班牙的牌组（oro） 中之只保留了硬币的花色
# Removes and returns the final element
suits.pop()

# Removes the first element that equals the argument
suits.remove('string')

# 然后又添加了三个新的花色
suits.append('cup')  # Add an element to the end
suits.extend(['sword', 'club'])  # Add all elements of a list to the end

# 意大利人把剑叫做“黑桃”
suits[2] = 'spade'  # Replace an element

# 传统的意大利牌组
print("传统的意大利牌组:", suits)

# 美国使用的法式变体修改了前两个
suits[0:2] = ['heart', 'diamond']  # Replace a slice
print("美国使用的法式变体:", suits)

print("Unicode字母表中的对应字符:", [lookup('WHITE ' + s.upper() + ' SUIT') for s in suits])


def make_mutable_rlist():
    """Return a functional implementation of a mutable recursive list."""
    contents = empty_rlist

    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_rlist(contents)
        elif message == 'getitem':
            return getitem_rlist(contents, value)
        elif message == 'push_first':
            contents = make_rlist(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return str(contents)

    return dispatch


def to_mutable_rlist(source):
    """Return a functional list with the same contents as source."""
    s = make_mutable_rlist()
    for element in reversed(source):
        s('push_first', element)
    return s


s = to_mutable_rlist(suits)
print(type(s))
print("自定义的列表:", s('str'))

print("删除第一个元素:", s('pop_first'))
print("自定义的列表:", s('str'))

