# Program to find a leap year
"""
Created on Tue Feb 10 12:45:27 2026

@author:Sanchita jadhav
"""

year=int(input("Enter year: "))
if(year% 400==0)or(year%4==0 and year%100!=0):
    print("leap year")
else:
    print("Not a Leap Year")
