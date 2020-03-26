#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: multiple_representation_2_7_2.py
@time: 2020/3/26 10:58
@desc: 2.7.2 多重表示
"""
from math import atan2, sin, cos, pi, gcd


def add_complex(z1, z2):
    return ComplexRI(z1.real + z2.real, z1.imag + z2.imag)


def mul_complex(z1, z2):
    return ComplexMA(z1.magnitude * z2.magnitude, z1.angle + z2.angle)


class ComplexRI(object):
    """复数表示：实部+虚部"""

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return 'ComplexRI({0}, {1})'.format(self.real, self.imag)


class ComplexMA(object):
    """复数表示：模+角度"""

    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        return 'ComplexMA({0}, {1})'.format(self.magnitude, self.angle)


print(add_complex(ComplexRI(1, 2), ComplexMA(2, pi / 2)))
print(mul_complex(ComplexRI(0, 1), ComplexRI(0, 1)))

ComplexRI.__add__ = lambda self, other: add_complex(self, other)
ComplexMA.__add__ = lambda self, other: add_complex(self, other)
ComplexRI.__mul__ = lambda self, other: mul_complex(self, other)
ComplexMA.__mul__ = lambda self, other: mul_complex(self, other)

print(ComplexRI(1, 2) + ComplexMA(2, 0))
print(ComplexRI(0, 1) * ComplexRI(0, 1))


class Rational(object):
    """有理数表示：分子+分母"""

    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)


def add_rational(x, y):
    nx, dx = x.numer, x.denom
    ny, dy = y.numer, y.denom
    return Rational(nx * dy + ny * dx, dx * dy)


def mul_rational(x, y):
    return Rational(x.numer * y.numer, x.denom * y.denom)


def iscomplex(z):
    return type(z) in (ComplexRI, ComplexMA)


def isrational(z):
    return type(z) == Rational


def add_complex_and_rational(z, r):
    return ComplexRI(z.real + r.numer / r.denom, z.imag)


def add_rational_and_complex(r, z):
    return add_complex_and_rational(r, z)


def add(z1, z2):
    """Add z1 and z2, which may be complex or rational."""
    if iscomplex(z1) and iscomplex(z2):
        return add_complex(z1, z2)
    elif iscomplex(z1) and isrational(z2):
        return add_complex_and_rational(z1, z2)
    elif isrational(z1) and iscomplex(z2):
        return add_complex_and_rational(z2, z1)
    else:
        return add_rational(z1, z2)


def type_tag(x):
    return type_tag.tags[type(x)]


type_tag.tags = {ComplexRI: 'com', ComplexMA: 'com', Rational: 'rat'}

add.implementations = {
    ('com', 'com'): add_complex,
    ('com', 'rat'): add_complex_and_rational,
    ('rat', 'com'): add_rational_and_complex,
    ('rat', 'rat'): add_rational}


def apply(operator_name, x, y):
    tags = (type_tag(x), type_tag(y))
    key = (operator_name, tags)
    return apply.implementations[key](x, y)


def mul_complex_and_rational(z, r):
    return ComplexMA(z.magnitude * r.numer / r.denom, z.angle)


mul_rational_and_complex = lambda r, z: mul_complex_and_rational(z, r)
apply.implementations = {
    ('mul', ('com', 'com')): mul_complex,
    ('mul', ('com', 'rat')): mul_complex_and_rational,
    ('mul', ('rat', 'com')): mul_rational_and_complex,
    ('mul', ('rat', 'rat')): mul_rational}

adders = add.implementations.items()
apply.implementations.update({('add', tags): fn for (tags, fn) in adders})

print(apply('add', ComplexRI(1.5, 0), Rational(3, 2)))
print(apply('mul', Rational(1, 2), ComplexMA(10, 1)))


def rational_to_complex(x):
    """强制转换"""
    return ComplexRI(x.numer / x.denom, 0)


coercions = {('rat', 'com'): rational_to_complex}


def coerce_apply(operator_name, x, y):
    tx, ty = type_tag(x), type_tag(y)
    if tx != ty:
        if (tx, ty) in coercions:
            tx, x = ty, coercions[(tx, ty)](x)
        elif (ty, tx) in coercions:
            ty, y = tx, coercions[(ty, tx)](y)
        else:
            return 'No coercion possible.'
    key = (operator_name, tx)
    return coerce_apply.implementations[key](x, y)


coerce_apply.implementations = {
    ('mul', 'com'): mul_complex,
    ('mul', 'rat'): mul_rational,
    ('add', 'com'): add_complex,
    ('add', 'rat'): add_rational}

print(coerce_apply('add', ComplexRI(1.5, 0), Rational(3, 2)))
print(coerce_apply('mul', Rational(1, 2), ComplexMA(10, 1)))
