# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:22:56 2026

@author: SANCHITA JADHAV
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def display(self):
        print("Current Balance:", self.balance)


# Example
acc = BankAccount(5000)

acc.deposit(1000)
acc.withdraw(2000)
acc.withdraw(5000)
acc.display()
