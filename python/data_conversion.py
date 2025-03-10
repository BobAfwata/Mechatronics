#!/usr/bin/env python

# ask the user for the first number 
first_number = int(input("Enter the first number :"))
second_number = int(input("Enter the second number :"))

sum_numbers = first_number + second_number
print(f"The sum of {first_number} and {second_number} is {sum_numbers}")


#print(type(first_number))


# convert string to integer  int()
# data types

# string : alphabet letters / numbers / special symbols in the keyboard :a,b....z ,ABCD.....Z ,01234...9 
# % * @ !&*  " " 

grade = 'A'
# strings 
my_name = "Bob"
#integers : positive / negative whole numbers

my_age = 24
temp = -13  

#float : positive / negative fractions / decimal point numbers  : 0.5
my_weight = 78.89

#boolean
# T / F two outputs : True / False
is_professor = False

is_married = True

print(type(grade))
print(type(my_weight))
print(type(my_age))
print(type(is_married))


# format the output 

print(f"My name is {my_name} and I am {my_age} years old ")

print("My name is {0} and I am {1} years old ".format(my_name,my_age))
