# first you have to import math module.

import math

# pi in math module.
math.pi

# e in math module.
math.e

# absolute value in built-in function in Python.
# abs()
abs(21)
abs(-21)

# round up in built-in function in Python.
# round()
round(1.3)
round(1.5)

# round down in math module.
# math.trunc()

import math
math.trunc(1.4)
math.trunc(1.5)
math.trunc(1.9)

# factorial in math module.
# math.factorial()
# example : 5! = 5x4x3x2x1

import math
math.factorial(1)
math.factorial(5)
math.factorial(10)

# degree in math module.
# math.degrees()

import math
math.degrees(math.pi)
math.degrees(math.pi/2)

# radian in math module.
# math.radians()

import math
math.radians(180)
math.radians(90)

# trigonometrical function in math module.
# math.cos(), math.sin(), math.tan(), math.acos(), math.asin(), math.atan()

import math
math.sin(math.radians(90))
math.cos(math.radians(180))
math.tan(math.radians(45))
math.tan(math.pi/4)
math.acos(-1)
math.asin(1.0)
math.atan(10000)

# square in bulit-in function in python or math module.
# ** (bulit-in) or math.pow() (math module)

import math
4 ** 2
4 ** 3
math.pow(4,2)
math.pow(4,3)

# square root in math module.
# math.sqrt

import math
math.sqrt(9)
math.sqrt(64)

# But sqrt() only use the square root of two.
# If you want to square root of over twe, you can use the math.pow() function.

27 ** (1/3)
math.pow(81,0.5)
math.pow(27,1/3)

# log in math module
# log() or log10()

import math
math.log(4,2)
math.log(math.e)
math.log(1000,10)
math.log10(1000)
