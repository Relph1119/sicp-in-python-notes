#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: interpreters_calc_3_5.py
@time: 2020/3/27 15:34
@desc: 3.5 组合语言的解释器-计算器的实现
"""
from functools import reduce
from operator import mul


class Exp(object):
    """
    A call expression in Calculator.
    usage:
        Exp('add', [1, 2])
        Exp('add', [1, 2])
        str(Exp('add', [1, 2]))
        'add(1, 2)'
        Exp('add', [1, Exp('mul', [2, 3, 4])])
        Exp('add', [1, Exp('mul', [2, 3, 4])])
        str(Exp('add', [1, Exp('mul', [2, 3, 4])]))
        'add(1, mul(2, 3, 4))'
    """

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)


def calc_apply(operator, args):
    """
    Apply the named operator to a list of args.
    usage:
        calc_apply('+', [1, 2, 3])
        6
        calc_apply('-', [10, 1, 2, 3])
        4
        calc_apply('*', [])
        1
        calc_apply('/', [40, 5])
        8.0
    """
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer / denom


def calc_eval(exp):
    """
    Evaluate a Calculator expression.
    usage:
        e = Exp('add', [2, Exp('mul', [4, 6])])
        e
        Exp('add', [2, Exp('mul', [4, 6])])
        calc_eval(e)
        26
    """
    if type(exp) in (int, float):
        return exp
    elif type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)


def tokenize(line):
    """
    Convert a string into a list of tokens.
    usage:
        tokenize('add(2, mul(4, 6))')
        ['add', '(', '2', ',', 'mul', '(', '4', ',', '6', ')', ')']
    """

    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.split()


def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')


def analyze_operands(tokens):
    """Read a list of comma-separated operands."""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands


def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token."""
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token


known_openrators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/']


def analyze(tokens):
    """
    Create a tree of nested lists from a sequence of tokens.
    usage:
        expression = 'add(2, mul(4, 6))'
        analyze(tokenize(expression))
        str(analyze(tokenize(expression)))
    """
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_openrators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected ' + token)


def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    # 标记序列，词法分析器
    tokens = tokenize(line)
    # 语法分析器
    expression_tree = analyze(tokens)

    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ''.join(tokens))
    return expression_tree


def read_eval_print_loop():
    """
    Run a read-eval-print loop for calculator.
    usage:
        calc> mul(1, 2, 3)
        6
        calc> add()
        0
        calc> add(2, div(4, 8))
        2.5
    """
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print('Calculation completed')
            return


if __name__ == '__main__':
    read_eval_print_loop()
