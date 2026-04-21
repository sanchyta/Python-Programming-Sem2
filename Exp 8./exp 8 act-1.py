# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:21:13 2026

@author: Sanchita jadhav
"""

balance = 5000  # example balance

try:
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        raise ValueError("Insufficient balance.")

    balance -= amount
    print("Withdrawal successful. Remaining balance:", balance)

except ValueError as e:
    print("Error:", e)