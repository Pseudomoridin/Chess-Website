# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 9th, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment
import math as m

def forceCalc(m, a):
    return m * a

def wavelength(d, a):
    return 2 * d * m.sin((a * m.pi) / 180)

def radioactiveDecay(time_decay, init_mass):
    half_life = 3.8
    return init_mass * (2**((time_decay * -1)/half_life))

def idealGasLaw(V,n,T):
    R = 8.314
    P = (n * R * T) / V
    return P / 1000