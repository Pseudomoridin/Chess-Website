# **Math 151**
## *Prof. Todd Schrader*
##### aka Master Frisbee Jesus
<br>

**Buy Webassign to do homework**  
NO CALCULATOR  
Quiz Sep 1 over syllabus  
<!-- DON'T MISS CLASS U DUM FUK -->
use link to sign up for webassign (website)  
HW due Thursdays  

---

## **Vectors**
### *"As I'm committing crimes with both direction and magnitude!"*
- Vector is something with both quantity and direction
    - 50mph west
- labeled by a letter with an arrow above it
- magnitude = length of a vector; 50 mph west, magnitude is 50
- vector written as ordered pair- x componenet and y component
- vector = (deltax, deltay)
- doesn't matter where the vector is drawn, at 0,0 is standard position
- as long as it has the same direction and magnitude, it is the same vector
- using ordered pair, use pythagorean to get magnitude
- vector \<2,5\> : magnitude = sqrt(2^2 + 5^2)
- > can use initial and terminal points to find vector: \<x2-x1,y2-y1\>
- find the vector first, then find the magnitude
- zero vector
    - has no magnitude or direction
- adding/subtracting/multiplying/dividing vectors
    - add vector notation x + x, y + y
    - add the actual vectors by putting the second vector at the tip of the other vector
        - not necessary to know, just nice
    - multiply vectors by scalar:
        - multiply each component of the vector by the scalar
        - amplification/reduction
        - multiply by negative, switches directions
    - subtracting vectors:
        - don't think of it as subtraction, think of it as adding a negative
        - > instead of AB - BC, AB + (BC * -1)
        - can also draw tip to tip or tail to tail
        - start both at standard position, resultant is vector from tip to tip
    - multiplying vectors by vectors:
        - use dot product
        - > **a dot b = |a||b|cos(theta)**
        - alternatively- multiply x components together and y components together, then add
        - dot product is always scalar
        - always use the shorter angle- will always be between 0 and pi
        - angle predicts sign:
            - dot product of a right angle is zero
            - dot product of an obtuse angle is negative
            - dot product of an acute angle is positive
        - orthogonal = perpendicular
        - if dot product is zero, vectors are orthogonal
        - **CAN COMBINE DOT PRODUCT FORMULAS TO FIND ANGLE**
            - > cos(theta) = (a dot b) / |a||b|
    - unit vectors:
        - has a magnitude of 1
        - divide vector by magnitude to get unit vector
        - > unit vector denoted by hat (a hat, p hat, AB hat, etc)
        - > to get a vector of any size, multiply unit vector by desired magnitude
- basis vectors:
    - can be used to build all other vectors
    - i is flat against x axis
    - j flat against y axis
    - another way of writing vectors
    - <2,3> = 2i + 3j
- parallel vectors
    - if a = constant * b, vectors parallel
    - solve x diff and y diff seperately for constant, if constants are equal vectors are parallel
- direction of vectors (theta):
    - vectors can be broken down into right triangles
    - if you have magnitude and angle, you can find vector notation with trig functions
    - ***vector a = <\|a\| \* cos(theta), \|a\| \* sin(theta)>***
    - radians not degrees <!-- (TT__TT) -->
    - get angle with inverse trig functions
    - get scalar with trig functions
    - without calculator, answer can contain trig functions
    - always use positive numbers then figure it out later, much easier
- bearings
    - everything measured north and south, angles measure deviation from north/south
    - N 45* W
    - S 89* E
    - think in opposite/adjacent, not x/y
- when mathing, always try to use data you **know** is correct
- orthogonal complement:
    - vector = <x, y>
    - vector' = <-y,x>
    - "special" perpindicular
- Work:
    - work = force * distance **WHEN FORCE AND DISTANCE ARE PARALLEL**
    - work = F dot d
    - work = Fdcos(theta)
    - work is the dot product of force and distance
- Projections:
    - The portion of b heading in the same direction as a
    - x = |b|cos(theta)
    - x = a dot b / |a| (scalar projection)
    - comp(sub a)b = a dot b / a
    x = (a dot b / |a|) * (a / |a|) (vector projection)
- Shortest distance from a point to a line
    - **SHORTEST DISTANCE IS ALWAYS PERPENDICULAR**
    - Could find line perpendicular then make it intersect point, find closest point on line & solve for distance
        - not good cause takes too long
    - find any vector that goes from line to point
    - find projection of the vector, you have distance
    - Vector Method
        - Vector for slope of the line
- Parametric functions
    - t is the independent variable
    - draw areas to show direction
    - x and y equations in terms of t
    - convert from parametric to cartesian by solving for t
    - with theta, solve for trig functions (sin, cos, tan, etc)
    - pythagorean identity very very useful (sin^2 + cos^2 = 1)
    - plug in points to find out directions
    - parametric vector functions
        - plug in values, get vectors
        - r(t) = <x(t),y(t)>
        - when drawing, plot points not vectors (endpoints of vectors)
        - r(t) = <x(t), y(t)>
            - x = x(t) and y = y(t), plot points from there
        - when getting position from vector functions, just change vector to coordinates
- Vector Equations
    - Vector equations can be broken into parametric equations
    - r = vectorr + t*vectorv 
        - (coefficient * t + constant)
    - find slope vector or direction vector
    - rnot is initial vector- convert point to vector {(2,5) to <2,5>}
    - r(t) = rnot + t * slope vector
    - r(t) = <rnotx, rnoty> + t<directionx, directiony>
        - Turn into parametric:
            - x = rnotx + t(directionx)
            - y = rnoty + t(directiony)
    - y = (m/n)x + b
    - r(t) = \<0,b\> + t\<n,m\>

---
## Example Problems
AB = \<4+2,1-5\> = \<6,-4\>  
AB = sqrt(6^2,-4^2) = sqrt(52)
<br></br>
a = \<3,-4\>, b = \<-1,2\>  
2a - b  
2\<3,-4\> + -1\<-1,2\>  
\<6,-8\> + \<1,-2\>  
2a - b = <7,-10>  
magnitude = sqrt(7^2 + -10^2)  
magnitude = sqrt(149)  
<br><br>
### Jet headed N 45* E at 760mph<br>Wind headed N 30* W at 40mph  
Jet = \<760sin(45), 760cos(45)\>  
Wind = \<-40sin(30), 40cos(30)\>  
Jet = \<380sqrt(2), 380sqrt(2)\>  
Wind = \<-20, 20sqrt(3)\>  
result = \<380sqrt(2) - 20, 380sqrt(2) + 20sqrt(3)\>
result = sqrt((380sqrt(2) - 20)^2 + (380sqrt(2) + 20sqrt(3))^2)
tan(alpha) = (380sqrt(2) - 20) / (380sqrt(2) + 20sqrt(3))
alpha = arctan((380sqrt(2) - 20) / (380sqrt(2) + 20sqrt(3)))
<br><br>
### Force 1 = 40, 60* from the x axis<br>Force 2 = 20, -30* from the x axis
F1 = <40cos(60), 40sin(60)>  
F2 = <20cos(30), -20sin(30)>  
F1 = <20, 20sqrt(3)>  
F2 = <10sqrt(3), -10>  
F3 = <20 + 10sqrt(3), 20sqrt(3) - 10>  
|F3| = sqrt((20 + 10sqrt(3))^2 + (20sqrt(3) - 10)^2)  
tan(theta) = (20sqrt(3) - 10) / (20 + 10sqrt(3))  
theta = tan^-1((20sqrt(3) - 10) / (20 + 10sqrt(3)))  