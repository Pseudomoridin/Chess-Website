# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 1st, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

import math as m

def quadratic(a,b,c):
    ima = b**2 - (4 * a * c)
    if ima < 0:
        imaginary = True
    else:
        imaginary = False
    ima = abs(ima)
    initroots = []
    initroots.append((-b + m.sqrt(ima)) / (2 * a))
    initroots.append((-b - m.sqrt(ima)) / (2 * a))
    trueRoots = []
    
    if initroots[0] == initroots[1]:
        initroots = [initroots[0]]

    if ima:
        for item in initroots:
            trueRoots.append(str(item) + "i")
    else:
        for item in initroots:
            trueRoots.append(str(item))
    return trueRoots

def linear(b,c):
    return

a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))

if a ==0 and b == 0 and c != 0:
    print("You entered an invalid combination of coefficients")
else:
    if a == 0:
        Quadratic = linear(b,c)
    else:
        Quadratic = quadratic(a,b,c)
    pluralizer = " is"
    formattedQuadratic = str(Quadratic[0])
    if len(Quadratic) > 1:
        pluralizer = "s are"
        formattedQuadratic += " and x = " + str(Quadratic[1])
    print("The root{} x = {}".format(pluralizer,formattedQuadratic))
