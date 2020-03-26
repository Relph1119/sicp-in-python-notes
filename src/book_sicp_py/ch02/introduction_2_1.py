#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: introduction_2_1.py
@time: 2020/3/25 8:55
@desc: 2.1 引言
"""

from datetime import date

today = date(2011, 9, 12)
print(date(2011, 12, 2) - today)
print(today.year)
print(today.strftime('%A, %B %d'))
print(type(today))

print("三个原始数值类型：整数(int)、实数(float)和复数(complex)")
print(type(2))
print(type(1.5))
print(type(1 + 1j))

