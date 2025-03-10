#!/usr/bin/env python 

# import the module 
import my_module 
import math
import os


print(my_module.first_name)
print(my_module.second_name)

my_module.tell_fav_team("Arsenal")
my_module.tell_name("Jada", "Elkasri")
my_module.tell_name("Moses", "Opuru")

bmi = my_module.calculate_bmi(87,115)
print(bmi)