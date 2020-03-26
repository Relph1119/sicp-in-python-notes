#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: elements_of_programming_1_2.py
@time: 2020/3/24 9:48
@desc: 1.2 编程元素
"""

print('max(7.5, 9.5) =', max(7.5, 9.5))

print('pow(100, 2) =', pow(100, 2))

print('pow(2, 100) =', pow(2, 100))

print('max(1, -2, 3, -4) =', max(1, -2, 3, -4))

print('max(min(1, -2), min(pow(3, 5), -4)) =', max(min(1, -2), min(pow(3, 5), -4)))

# 导入库函数

from math import sqrt, exp

print('sqrt(256) =', sqrt(256))

print('exp(1) =', exp(1))

from operator import add, sub, mul

print('14 + 28 =', add(14, 28))

print('100 - 7 * (8 + 4) =', sub(100, mul(7, add(8, 4))))

# 名称和环境
radius = 10
print(radius)
print(2 * radius)

# 通过import语句绑定
from math import pi

print('pi * 71 / 223 =', pi * 71 / 223)

# 在一个语句中将多个值赋给多个名称
area, circumference = pi * radius * radius, 2 * pi * radius
print('area =', area)
print('circumference =', circumference)

# 中序表达式
print('(2 + 4 * 6) * (3 + 5) =', mul(add(2, mul(4, 6)), add(3, 5)))
