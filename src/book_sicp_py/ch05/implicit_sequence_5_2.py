#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: implicit_sequence_5_2.py
@time: 2020/3/30 15:48
@desc: 5.2.1 Python迭代器
"""


class Letters(object):
    def __init__(self):
        self.current = 'a'

    def __next__(self):
        if self.current > 'd':
            raise StopIteration
        result = self.current
        self.current = chr(ord(result) + 1)
        return result

    def __iter__(self):
        return self


print("-----------迭代器-----------")
letters = Letters()
try:
    print(letters.__next__())
    print(letters.__next__())
    print(letters.__next__())
    print(letters.__next__())
    print(letters.__next__())
except Exception as e:
    print(e)


class Positives(object):
    def __init__(self):
        self.current = 0

    def __next__(self):
        result = self.current
        self.current += 1
        return result

    def __iter__(self):
        return self


def letters_generator():
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current) + 1)


print("-----------生成器-----------")
for letter in letters_generator():
    print(letter)

print("-----------可迭代对象-----------")


def all_pairs(s):
    for item1 in s:
        for item2 in s:
            yield (item1, item2)


print(list(all_pairs([1, 2, 3])))

class LetterIterable(object):
    def __iter__(self):
        current = 'a'
        while current <= 'd':
            yield current
            current = chr(ord(current) + 1)

letters = LetterIterable()
print(all_pairs(letters).__next__())