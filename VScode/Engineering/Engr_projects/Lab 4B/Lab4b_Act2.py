# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:          Elayne Elphingstone
# Section:       572
# Assignment:    Lab1b, Act 2
# Date:          September 1st, 2021

#This file is the intellectual property of Elayne Elphingstone and anyone submitting the same file will be sued for copyright infringment

# I refuse to put imports anywhere but at the top
from math import sqrt

########### Part A ##########
# I added the comments cause I thought they were funny
# I did type it although I copied the comments
a = 1/7 # I SAID TYPE, NOT COPY/PASTE!
print('a =', a) # NEVER COPY/PASTE CODE YOU DIDN’T WRITE
b = a * 7 # ESPECIALLY NOT FROM THE INTERNET
print("b = a * 7 =", b)
""" Wow it's 1 who could've guessed this would happen """

########### Part B ##########
c = 2 * a # DID YOU COPY/PASTE AGAIN?
d = 5 * a # TYPE THE CODE!
f = c + d # DON’T BE LAZY!
print("f = 2 * a + 5 * a =", f)
""" It's not 1 cause floats are just rough(for a computer) approximations of the actual number """

########### Part C ##########
x = sqrt(1 / 3) # STILL COPY/PASTING?
print("x =", x) # THIS IS GOOD PRACTICE FOR TYPING!
y = x * x * 3 # YOU’LL REMEMBER IT BETTER IF YOU TYPE
print("y = x * x * 3 =", y)
z = x * 3 * x # INSTEAD OF COPY/PASTE!
print("z = x * 3 * x =", z)
""" They aren't both 1 cause floats """

TOL = 1e-10
if abs(b - f) < TOL: # WHEN YOU COPY/PASTE, ‘ MAY BE WRITTEN FUNNY
    print("b and f are equal within tolerance of", TOL)
else: # YET ANOTHER REASON TO TYPE THE CODE!
    print("b and f are NOT equal within tolerance of", TOL)

if abs(b - f) < TOL:
    print("y and z are equal within tolerance of", TOL)
else:
    print("y and z are NOT equal within tolerance of", TOL)

m = 0.1 # AGGIES DO NOT LIE, CHEAT, OR STEAL,
print("m =", m) # OR TOLERATE THOSE WHO DO
n = 3 * m # BE AN AGGIE
print("n = 3 * m = 0.3", n == 0.3)
p = 7 * m # ALWAYS WRITE YOUR OWN CODE """I am I just think this is funny"""
print("p = 7 * m = 0.7", p == 0.7)
q = n + p
print("q = 1", q == 1)
""" I love floats, they make no sense and screw everything up. Use Decimals when you need exact accuracy """
