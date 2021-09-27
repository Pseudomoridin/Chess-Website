# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 1st, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment
import random
import math

print("This shows the evaluation of (e^x-1)/x evaluated close to x=0")
print("My guess is 0.")

x = "1"
xfloat = 1
while xfloat >= 10**-7:
    print("value at",xfloat,"is",(math.e**(xfloat) - 1) / xfloat)
    xfloat = float("0." + x)
    x = "0" + x

print("\nMy random guess was exactly as good as expected.")