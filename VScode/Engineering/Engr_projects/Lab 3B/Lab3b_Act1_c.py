# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 9th, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

from functions import radioactiveDecay

print("This program calculates how much Radon-222 is left given time and initial amount")
time = float(input("Please enter the time (days): "))
mass = float(input("Please enter the initial amount (g): "))
radon = radioactiveDecay(time, mass)
print("Radon-222 left is {:.2f} g".format(radon))