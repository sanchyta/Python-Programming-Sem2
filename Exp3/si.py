# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:29:34 2026

@author: Sanchita Jadhav
"""
def simple_interest(principal,rate,time):
    si=(principal*rate*time)/100
    return si
#Taking input from the user 
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter time(in years):"))
#Function call
interest=simple_interest(p,r,t)
print("Simple Interest is:",interest)
