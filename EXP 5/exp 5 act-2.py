# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:11:10 2026

@author: Sanchita Jadhav
"""

# Roll numbers in two classes
class_A = {1, 2, 3, 4, 5}
class_B = {4, 5, 6, 7, 8}

# Students present in both classes
common_students = class_A.intersection(class_B)

print("Students in both classes:", common_students)