#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: mutable_data_2_4.py
@time: 2020/3/25 16:06
@desc: 2.4 可变数据
"""


# 1.局部状态
# withdraw 的函数来实现它，它将要取出的金额作为参数。
# 如果账户中有足够的钱来取出，withdraw 应该返回取钱之后的余额。
# 否则， withdraw 应该返回消息 'Insufficient funds'
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance  # Declare the name "balance" nonlocal
        if amount > balance:
            return 'Insufficient funds'
        balance -= amount  # Re-bind the existing balance name
        return balance

    return withdraw


withdraw = make_withdraw(100)
print("初始账户里面有100元")
print("取出25元，还剩下{}元".format(withdraw(25)))
print("取出25元，还剩下{}元".format(withdraw(25)))
print("取出60元，{}".format(withdraw(60)))
print("取出15元，还剩下{}元".format(withdraw(15)))
