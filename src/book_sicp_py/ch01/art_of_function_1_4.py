#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: art_of_function_1_4.py
@time: 2020/3/24 10:23
@desc: 1.4 实践指南：函数的艺术
"""


def pressure(v, t, n):
    """Compute the pressure in pascals of an ideal gas.
    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law
    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas
    """
    k = 1.38e-23  # Boltzmann's constant
    return n * k * t / v


help(pressure)

k_b = 1.38e-23


def pressure(v, t, n=6.022e23):
    """Compute the pressure in pascals of an ideal gas.
    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas (default: one mole)
    """
    return n * k_b * t / v


print(pressure(1, 273.15))
