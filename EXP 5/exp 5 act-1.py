# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:10:20 2026

@author: Sanchita Jadhav
"""

# Library dictionary
library = {
    "Python Basics": 250,
    "Data Science": 500,
    "AI Fundamentals": 750
}

# Update price
book_name = "Data Science"
new_price = 550

if book_name in library:
    library[book_name] = new_price

print("Updated Library:", library)