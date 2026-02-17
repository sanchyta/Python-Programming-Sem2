# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 06:40:00 2026

@author: Sanchita Jadhav
"""
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
