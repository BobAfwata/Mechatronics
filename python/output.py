#!/usr/bin/env python

# strings  : a collection of characters 

#1  using curly brackets  {} and .format()
name = input("Enter your name : ")
city = input("Where are you from ? :")
height = input("Enter your height")

print("My name is  {0} and I am from {1} and I {2} cm tall ".format(name ,city,height))
print("My name is  {2} and I am from {1} and I {0} cm tall ".format(name ,city,height))


#2 f string  print(f" I am {name}")
print(f"My name is  {name} and I am from {city} and I {height} cm tall ")

f_string = f" I am {name} and I measure {height} in cms"
print(f_string)

#snake case
favorite_team = "Man U" 
first_name = "Bob"


# camel case
secondName = "Afwata"
cityOfOrigin = "Arush"
weight = 67.2 

# 2 format specifiers
# %d -integers - positive and negative whole numbers 
# %s strings and characters 
# %f float - fractions / decimal points -- 12.890

t = 8           #integer  %d
club = "Arsenal" #string  %s
w = 140.90    #floating   %f
print("My favourite club is  %s and I weigh %f " %(club,w))

print(" I am  %s and I weigh %f " %(first_name,weight))




age = 34
fav_food = "fish"
hobby = "dancing"

print(f" I am {age} years old and my fav food is {fav_food} and my hobby is {hobby}")

pi = 3.1425787
print(f"The value of pi is {pi }")
print("The value of pi is %.3f" %(pi))
print("The value of pi is %.2f" %(pi))


#food = "Chapati"
#calories = 70
print("I like {} and it has {}  calories".format(food="Chapati",calories =70))
print("She like {} and it has {}  calories".format(food = "rice",calories = 60))