#!/usr/bin/env python 

# variables in the module
first_name  = "Bob"
second_name = "Afwata"

fav_team    = "Man City"
weight      = 78
height      = 120
hobby       = "swimming"

friends = ["Lisa", "John","Moses" ,"Emmanuel"]
# functions

def tell_name(first_name,second_name):
    print(f" My name is {first_name} {second_name}")

def tell_fav_team(fav_team):
    print(f" I am a big {fav_team} fan")

def calculate_bmi(weight,height):
    bmi = weight / (height ** 2)
    return bmi