# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 9th, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

import math as m

def get_lengths_from_area(area):
    radius = m.sqrt(area/m.pi)
    tri = m.sqrt((4/m.sqrt(3)) * area)
    square = m.sqrt(area)
    penta = m.sqrt((4 * area) / m.sqrt(5 * (5 + m.sqrt(20))))
    dodeca = m.sqrt(area / (3 * (2 + m.sqrt(3))))
    return [radius, tri, square, penta, dodeca]

area = float(input("Please enter the area: "))
side_lengths = get_lengths_from_area(area)
print("A circle with area {:.2f} has a radius {:.3f}".format(area, side_lengths[0]))
print("An equilateral triangle with area {:.2f} has a side {:.3f}".format(area, side_lengths[1]))
print("A square with area {:.2f} has a side {:.3f}".format(area, side_lengths[2]))
print("A pentagon with area {:.2f} has a side {:.3f}".format(area, side_lengths[3]))
print("A dodecagon with area {:.2f} has a side {:.3f}".format(area, side_lengths[4]))
