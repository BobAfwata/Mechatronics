#!/usr/bin/env python 
from array import *

# arrays 
# arrays start at 0

ages = array('i' ,[23,45,67,78,89,29]) # i - integers

print(ages[0])
print(ages[1])

"""
print(ages[0])
print(ages[1])
print(ages[5])
print(ages[-1])
"""


print(ages)
ages.append(73)
ages.append(63)
ages.append(71)
print(ages)

ages[2] = 75

ages.pop() # removes the last item in the array
ages.pop()
print(ages)

print(len(ages)) #size of array (how may items are in the array)

ages.reverse()
print(ages)

for i in ages:
    print(i)

#print(ages[6]) # out of index error

#print(len(ages)) # 6 items
# create an array of 5 numbers




#list
our_ages = [23,56,67,89,12,67]