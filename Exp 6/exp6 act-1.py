# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:38:46 2026

@author: Sanchita jadhav
"""
file_name = "expenses.txt"

# Step 1: Take daily expenses input and store in file
n = int(input("Enter number of days: "))

with open(file_name, "w") as file:
    for i in range(n):
        expense = float(input(f"Enter expense for day {i+1}: "))
        file.write(str(expense) + "\n")

print("Expenses saved successfully.\n")

# Step 2: Read file and calculate total expense
total = 0
with open(file_name, "r") as file:
    for line in file:
        total += float(line.strip())

print("Total Monthly Expense:", total)
