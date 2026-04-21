# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:15:16 2026

@author: sanchita jadhav
"""

file_name = "expenses.txt"

# Step 1: Write daily expenses
with open(file_name, "w") as file:
    file.write("100\n200\n150\n300\n250\n")  # example daily expenses

# Step 2: Read and calculate total
total = 0
with open(file_name, "r") as file:
    for line in file:
        total += int(line.strip())

print("Total Monthly Expense:", total)