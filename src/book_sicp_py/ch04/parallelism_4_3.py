#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: parallelism_4_3.py
@time: 2020/3/30 15:38
@desc: 4.3 并行计算
"""

from threading import Lock


def make_withdraw(balance):
    balance_lock = Lock()

    def withdraw(amount):
        nonlocal balance
        # try to acquire the lock
        balance_lock.acquire()
        # once successful, enter the critical section
        if amount > balance:
            print("Insufficient funds")
        else:
            balance = balance - amount
            print(balance)
        # upon exiting the critical section, release the lock
        balance_lock.release()


from threading import Semaphore

db_semaphore = Semaphore(2)  # set up the semaphore
database = []


def insert(data):
    db_semaphore.acquire()  # try to acquire the semaphore
    database.append(data)  # if successful, proceed
    db_semaphore.release()  # release the semaphore


insert(7)
insert(8)
insert(9)
