# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 9th, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

from functions import wavelength

print("This program calculates the wavelength given distance and angle")
d = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
wvl = wavelength(d, angle)
print("Wavelength is {:.4f} nm".format(wvl))