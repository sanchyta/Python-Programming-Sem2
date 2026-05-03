# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:22:56 2026

@author: SANCHITA JADHAV
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


# Example
stu = Student("Sanchita", 82)
stu.display()
