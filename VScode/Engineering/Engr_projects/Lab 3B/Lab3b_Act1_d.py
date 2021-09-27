# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 9th, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

from functions import idealGasLaw

print("This program calculates the pressure given moles, volume, and temperature")
n = float(input("Please enter the number of moles: "))
V = float(input("Please enter the volume (m^3): "))
T = float(input("Please enter the temperature (K): "))
P = idealGasLaw(V,n,T)
print("Pressure is {:.0f} kPa".format(P))