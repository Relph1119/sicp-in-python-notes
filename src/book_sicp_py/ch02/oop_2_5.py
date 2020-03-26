#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: oop_2_5.py
@time: 2020/3/26 9:29
@desc: 2.5 面向对象编程
"""


class Account(object):
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


print("创建Jim的账户")
a = Account('Jim')
print("账户所有者:", a.holder)
print("账户金额:", a.balance)
print("---------------")

print("创建Jack的账户")
b = Account('Jack')
b.balance = 200
print("Jim和Jack的账户金额:", [acc.balance for acc in (a, b)])
print("---------------")

print("创建Tom的账户")
tom_account = Account('Tom')
print("存入100元")
tom_account.deposit(100)
print("取出90元")
tom_account.withdraw(90)
print("再取出90元")
tom_account.withdraw(90)
print("账户所有者:", tom_account.holder)

print("Tom账户金额:", getattr(tom_account, 'balance'))
print(hasattr(tom_account, 'deposit'))