#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: inheritance_2_5_5.py
@time: 2020/3/26 10:05
@desc: 2.5.5 继承
"""


class Account(object):
    """A bank account that has a non-negative balance."""
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)


print("创建Sam的Checking账号")
checking = CheckingAccount('Sam')
print("存入10元")
checking.deposit(10)
print("取出5元")
print("剩余金额{}元".format(checking.withdraw(5)))
print(checking.interest)


class SavingsAccount(Account):
    deposit_charge = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)


class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.holder = account_holder
        self.balance = 1  # A free dollar!

print("-------------------")
print("创建John的SeenOnTV账户")
such_a_deal = AsSeenOnTVAccount("John")
print("赠送{}元".format(such_a_deal.balance))
print("存入20元")
such_a_deal.deposit(20)
print("消费5元")
such_a_deal.withdraw(5)

print([c.__name__ for c in AsSeenOnTVAccount.mro()])