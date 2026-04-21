# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:17:03 2026

@author: Sanchita jadhav
"""

file_name = "complaints.txt"

# Step 1: Create a complaint file (example)
with open(file_name, "w") as file:
    file.write("Late delivery\n")
    file.write("Damaged product\n")
    file.write("Wrong item received\n")

# Step 2: Read and display complaints
print("Customer Complaints:")
with open(file_name, "r") as file:
    for complaint in file:
        print(complaint.strip())