# Calculating Stress from Strain
## The equations
- for x > 0, print error: invalid value and exit
- for 0 <= x < .01, f(x) = 4300x
- for 0.01 <= x < 0.06, f(x) = 10x + 42.9
- for 0.06 <= x < 0.18, f(x) = 137.5x + 35.25
- for 0.18 <= x <= 0.27, f(x) = -100x + 78
- else, print error: steel broke and exit
## The test cases
- Negative number
- Points in the middle of each range
- Points on the edges of each range
- Points where the steel would break
## The variables
- Strain
- Stress
## The steps
- Get input for the strain
- Check if strain input is valid
- Check each range if the strain is in it
- Use the correct equation to return stress