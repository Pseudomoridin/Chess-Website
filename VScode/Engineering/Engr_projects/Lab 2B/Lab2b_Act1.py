# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 9th, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment
import math

#Force calculation
m = 2
a = 5
print ("Force is",m * a,"N")

#x-ray wavelength
scattering_angle = float(25 * math.pi) / 180
layer_thickness = 0.025
print ("Wavelength is",2 * layer_thickness * math.sin(scattering_angle),"nm")

#Radon-222 decay
init_mass = 3.0
half_life = 3.8
time_decay = 5.0
print("Radon-222 left is",init_mass * (2**((time_decay * -1)/half_life)),"g")

#ideal gas law
#PV = nRT
V = .15
n = 5
R = 8.314 / 1000
T = 425
print ("Pressure is",(n * R * T)/V,"kPa")