# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab 2B
# Date:          September some point, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

def getx(time):
    return XSLOPE * time + XYINT
def gety(time):
    return YSLOPE * time + YYINT
def getz(time):
    return ZSLOPE * time + ZYINT

time0 = 30
time1 = 60

timestep = (time1 - time0) / 4

x = 0
XSLOPE = 23 / 73
XYINT = 2 - (XSLOPE * 12)
y = 0
YSLOPE = -8 / 73
YYINT = 3 - (YSLOPE * 12)
z = 0
ZSLOPE = 4 / 73
ZYINT = 7 - (ZSLOPE * 12)

for x in range(5):
    print("At time",time0 + (x * timestep),"seconds:")
    print ("x0 =",getx(time0 + (x * timestep)),"m")
    print ("y0 =",gety(time0 + (x * timestep)),"m")
    print ("z0 =",getz(time0 + (x * timestep)),"m")
    if x != 4:
        print("----------------------")