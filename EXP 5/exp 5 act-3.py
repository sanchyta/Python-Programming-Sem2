# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:12:01 2026

@author: sanchita jadhav
"""

# Inventory dictionary
inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 20
}

# Add new stock
item = "Bananas"
quantity_to_add = 25

if item in inventory:
    inventory[item] += quantity_to_add
else:
    inventory[item] = quantity_to_add

print("Updated Inventory:", inventory)