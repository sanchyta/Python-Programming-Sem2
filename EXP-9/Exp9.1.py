# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:22:56 2026

@author: SANCHITA JADHAV
"""
import math

# Input
p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (%): ")) / 100 / 12
n = int(input("Enter number of months: "))

# EMI Formula
emi = (p * r * math.pow(1 + r, n)) / (math.pow(1 + r, n) - 1)

print("Monthly EMI:", emi)
