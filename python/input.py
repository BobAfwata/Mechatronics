#!/usr/bin/env python 
import math 

#f string
"""
for i in range(0,5):
    name = input("Enter  your name : ")
    age = input("enter your age : ")
    print(f"My name is {name} and I am {age} years old")
"""
# this is a single line comment 

""" 
Multi line comment 
angle = 30
math.cos(angle)

print("--------------------------------------------------------------------------")
print("|      i     |   cos(i)      | sin(i)         |        tan(i)|")
for i in range(-180, 180, 30 ):
    print("------------------------------------------------------------------------")
    print(f"| {i}  | {math.cos(i)} | {math.sin(i)} | {math.tan(i)} | ")

"""

#print the powers of numbers from 1 to 10 in a tabular form using for loop 
print("---------------------------------------")
print("x^1\tx^2\tx^3\tx^4\tx^5")
for i in range(1,11):
    print(f"{i}\t{math.pow(i,2)}\t{math.pow(i,3)}\t{math.pow(i,4)}\t{math.pow(i,5)}")
    print("-------------------------------------------")


print("----------------------------------------------------------")

#tabs and new lines 
print("NewYork\tSeoul\tNairobi\tDar-esalaam\tJuba\tKampala")
print("1\t2\t3\t4\t5\t6\t200")

#  \t new tab 
# \n new line 
print("My name is \n Bob \n Afwata")
print("NewYork\nSeoul\nNairobi\nDar-esalaam\nJuba\nKampala")