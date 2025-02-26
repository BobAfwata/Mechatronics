#!/usr/bin/env python
import math 
# function - block of code / statements executed together 
# function definition

name = "Bob Afwata"
country = "Kenya"
age = 24

#function 
def print_details(name,age,country):
    #body of the function
    print(f"My name is {name} ")   # line of code - statement of code
    print(f"I am {age} years old") # line of code - statement of code
    print(f"I am from {country} ") # line of code - statement of code 

print_details("Moses",24,"Kenya")
print_details("Jada",22,"Morocco")
print_details("Emmanuel",30,"Tanzania")

def add_numbers(x,y):
    return x + y

def multiply_numbers(x,y):
    return x * y


# call the functions
sum_numbers = add_numbers(10,30)
product_numbers = multiply_numbers(50,12)
print(sum_numbers)
print(product_numbers)

# write a function to calculate volue of cylinder

def volume_cylinder(radius,height,pi):
    volume = pi * radius * radius * height
    return volume


v = volume_cylinder(70,50,math.pi)
print(v)
# area of circle

