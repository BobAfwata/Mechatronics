#!/usr/bin/env python 

# program to calculate the factorial of a number using while loop

number = int(input("Enter the number : ")) # promt user 

fact_n = 1 #factorial of n
while number >=1 :
    fact_n = number * fact_n  # n! = n * (n-1)
    number = number - 1 # (n-1)
    
print(fact_n)
    