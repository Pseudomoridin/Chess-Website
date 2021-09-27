# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 9th, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

from functions import forceCalc

print("This program calculates the applied force given mass and acceleration")
m = float(input("Please enter the mass (kg): "))
a = float(input("Please enter the acceleration (m/s^2): "))
F = forceCalc(m, a)
print("Force is {:.1f} N".format(F))