# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 1st, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

def wingdings(days):
    if days > 100:
        return 3820 # Will always be constant no matter how many extra days
    elif days > 50:
        return 100 + (((50-10)/2) * (50 + 11)) + (50 * (days - 50))
    elif days > 10:
        return 100 + (((days - 10) / 2) * (days + 11))
    else:
        return 10 * days

days = int(input("Please enter a positive value for day: "))
if days < 0:
    print("You entered an invalid number!")
else:
    print("The total number of widgets produced on day {0} is {1:.0f}".format(days,wingdings(days)))

"""
# We wanna do this without the loop
day = 0
widgets = 0
while days != 0:
    day += 1
    days -= 1
    if day > 100:
        continue
    elif day >= 50:
        widgets += 50
    elif day > 10:
        widgets += day
    else:
        widgets += 10
# """
