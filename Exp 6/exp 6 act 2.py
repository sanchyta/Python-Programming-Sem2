# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:16:10 2026

@author: Sanchita jadhav
"""

file_name = "attendance.txt"

# Step 1: Create file with initial records
with open(file_name, "w") as file:
    file.write("Roll No - 1: Present\n")
    file.write("Roll No - 2: Absent\n")

# Step 2: Append new records
with open(file_name, "a") as file:
    file.write("Roll No - 3: Present\n")
    file.write("Roll No - 4: Present\n")

print("Attendance records updated successfully.")

# Display content
with open(file_name, "r") as file:
    print(file.read())