#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: coroutine_5_3.py
@time: 2020/3/30 16:33
@desc: 5.3 协程
"""


def match(pattern):
    """
    用于打印匹配所提供的模式串的字符串
    :param pattern:
    :return:
    """
    print('Looking for ' + pattern)
    try:
        while True:
            s = (yield)
            if pattern is s:
                print(s)
    except GeneratorExit:
        print('=== Done ===')


m = match('Jabberwock')
m.__next__()
m.send("the Jabberwock with eyes of flame")
m.send("came whiffling through the tulgey wood")
m.send("and burbled as it came")
m.close()

text = 'Commending spending is offending to people pending lending!'
matcher = match('ending')
matcher.__next__()


# read(text, matcher)

def match_filter(pattern, next_coroutine):
    print('Looking for ' + pattern)
    try:
        while True:
            s = (yield)
            if pattern in s:
                next_coroutine.send(s)
    except GeneratorExit:
        next_coroutine.close()


def print_consumer():
    print('Preparing to print')
    try:
        while True:
            line = (yield)
            print(line)
    except GeneratorExit:
        print("=== Done ===")


printer = print_consumer()
printer.__next__()
matcher = match_filter('pend', printer)
matcher.__next__()


# read(text, matcher)

def count_letters(next_coroutine):
    try:
        while True:
            s = (yield)
            counts = {letter: s.count(letter) for letter in set(s)}
            next_coroutine.send(counts)
    except GeneratorExit as e:
        next_coroutine.close()


def sum_dictionaries():
    total = {}
    try:
        while True:
            counts = (yield)
            for letter, count in counts.items():
                total[letter] = count + total.get(letter, 0)
    except GeneratorExit:
        max_letter = max(total.items(), key=lambda t: t[1])[0]
        print("Most frequent letter: " + max_letter)


s = sum_dictionaries()
# s.__next__()
c = count_letters(s)


# c.__next__()
# read(text, c)

def read_to_many(text, coroutines):
    for word in text.split():
        for coroutine in coroutines:
            coroutine.send(word)
    for coroutine in coroutines:
        coroutine.close()


m = match("mend")
m.__next__()
p = match('pe')
p.__next__()
read_to_many(text, [m, p])
