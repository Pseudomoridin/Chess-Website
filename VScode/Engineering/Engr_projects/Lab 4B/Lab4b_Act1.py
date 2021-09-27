# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 1st, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

# method definition
def smallest(nums):
    smol = 99999
    for item in nums:
        if item < smol:
            smol = item
    return smol

# variable definition
a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))
nums = [a,b,c]

print("The smallest number is {}".format(smallest(nums)))