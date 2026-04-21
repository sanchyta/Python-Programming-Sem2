# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:21:54 2026

@author: sANCHITA JADHAV
"""

try:
    age = int(input("Enter your age: "))

    if age <= 0:
        raise ValueError("Age must be positive.")

    print("Registration successful. Age:", age)

except ValueError:
    print("Error: Please enter a valid positive integer for age.")