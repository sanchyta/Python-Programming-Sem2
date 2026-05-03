# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:22:56 2026

@author: SANCHITA JADHAV
"""
import math

# Input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Distance Formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance between points:", distance)
