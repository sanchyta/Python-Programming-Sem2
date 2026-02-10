# Bill program
"""
Created on Tue Feb 10 13:29:14 2026

@author:Sanchita Jadhav
"""
u=int(input("Enter units:"))
if u<=100:
    bill=0
elif u<=200:
    bill=(u-100)*5
else:
    bill=500+(u-200)*10
    print("Bill=",bill)
