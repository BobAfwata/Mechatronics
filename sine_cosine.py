#!/usr/bin/env python 

# write a program using math libary to
#  print the sine ,cosine ,tangeng of angles from - 180 -> + 180  
import math 

angle = 90

for angle in range(-180,180,30):
    print(math.sin(angle))
    print(math.cos(angle))
    print(math.tan(angle))

