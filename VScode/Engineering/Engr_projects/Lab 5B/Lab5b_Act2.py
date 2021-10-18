# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    No clue
# Date:          September some point, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

# Getting strain input
strain = float(input("Enter the strain: "))

# Using ranges of strain to pick correct equation\
# check if valid
if strain < 0:
    print("Strain is undefined in that region")
    exit()
# "Elastic region" / Young's modulus
if strain < 0.01:
    stress = 4300 * strain
# "Plastic" region
elif strain < 0.06:
    stress = (10 * strain) + 42.9
# "Strain-hardening" region
elif strain < 0.18:
    stress = (137.5 * strain) + 35.25
# "Necking" region
elif strain <= 0.27:
    stress = (-100 * strain) + 78
# Fracture point
else:
    print("The steel broke!")
    exit()

print("The stress is approximately {:.1f}".format(stress))
