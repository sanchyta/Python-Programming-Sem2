# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 07:22:56 2026

@author: SANCHITA JADHAV
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        bonus = 0.1 * self.salary   # 10% bonus
        total_salary = self.salary + bonus
        return total_salary

    def display(self):
        print("Name:", self.name)
        print("Total Salary with Bonus:", self.calculate_salary())


# Example
emp = Employee("Sanchita", 20000)
emp.display()
