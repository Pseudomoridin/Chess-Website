# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 9th, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

# Because of how floating point numbers work, this lab is impossible using them, since they are only approximations
# So, I used Decimals, which store exact numbers, to avoid having to use round.

import math as m
from decimal import Decimal

def redefine_Round(_num, float_digits):
    num = Decimal(_num)
    tentothedigit = Decimal(10)**Decimal(-float_digits)
    if num % (tentothedigit) >= Decimal(5 * 10 ** -(float_digits + 1)):
        num = (num // tentothedigit)
        num = num * tentothedigit
        add = tentothedigit
        num = num + add
    else:
        num = (num // tentothedigit)
        num = num * tentothedigit
    return num

digits = int(input("Please enter the number of digits of precision for pi: "))
print("The value of pi to {} digits is: {}".format(digits,str(redefine_Round(m.pi, digits))))