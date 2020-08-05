"""
Lambdata - A collection of classes for Dataframe
"""

# Helper Link: https://youtu.be/ZDa-Z5JzLYM
# content: class, instances of a class,
# instance variables of an instance in a class
# class variables


import pandas as pd
import numpy as np


class Employee:

    num_of_employees = 0  # Head to __init__
    raise_amount = 1.04
    # Class Variables, shared between a class and its subclass(es)

    def __init__(self, first, last, pay):  # __init__() is the constructor
        """Instance of class Employee"""

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        """Class Instance Variables, unique to each instance"""

        Employee.num_of_employees += 1

    def fullname(self):
        return '{}, {}'.format(self.last, self.first)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # self.pay = int(self.pay * self.raise_amount) # 2nd way

    @classmethod
    # Classmethod uses a decorator (@) to alter the functionality of the method
    # now the class is received instead of the instance
    def set_raise_amount(cls, amount):  # cls = class
        cls.raise_amount = amount

class Complex:
    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.imaginary = imaginary_part

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __repr__(self):
        return f"({self.real}, {self.imaginary})"

    def __add__(self, other_inst):
        real = self.real + other_inst.real
        imaginary = self.imaginary + other_inst.imaginary
        return f"{real} + {imaginary}i"


print(Employee.num_of_employees)  # For use w/similar print statement below
# Comparison on the # of emps for Employee class (before employees)

emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
# Instead of below, short w/above.
######################################
# emp_1.first = 'Corey'
# emp_1.last = 'Shafer'
# emp_1.email = 'Corey.Shafer@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000
#######################################

# print(emp_1)
# print(emp_1)


print(emp_1.email)
print(emp_2.email)


print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
# print(emp_1.fullname())# 2nd way
# print(emp_2.fullname())# 2nd way

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# When we try to access an attribute on an instance,
# it will first check if that instance contains that attribute,
# and if it doesn't,
# then it will see if the class or any class that it inherits
# from contains that attrribute.
# So, when you access raise_amount from our instances,
# they don't actually have that atrribute themselves,
# they're accessing the classes
# raise_amount attribute.

# See below to really see what is going on
print(emp_1.__dict__)  # on purpose
print(Employee.__dict__)


print(Employee.num_of_employees)  # For use w/similar print statement above
# Comparison on the # of emps for Employee class (after employees)

# now the class is received instead of the instance
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
