#!/usr/bin/env python

# list of fruits 
# mutable - size / content one can change the size 
# array === same to lists
# list_name = [""]
fruits = ["Lemon", "Orange","Apple","Kiwi","Peaches","Mangoes","Guavas"] #string
#            -7          -6        -5    -4   -3      -2         -1
cities = ["Nairobi","Khartoum","Algiers","Rabat"]

friends = ["Jada","Riak","Moses","Emmanuel"]

print(fruits)
print(friends)  
print(cities)  

print(type(fruits))
fruits[0] = "Banana"
print(fruits) 

fruits[-3] = "Pineapple"
print(fruits) 

# for loop to print all fruits 

for fruit in fruits:
    print(fruit)

fruits.append("Water Mellon")
fruits.append("Lime")
fruits.append("Avocado")

print(fruits)
fruits.pop() # removes last item
print(fruits)
fruits.pop()
print(fruits)


fruits.insert(3,"Pawpaw")

fruits.extend(["Tomatoes","Cherry","Grapes"])
print(fruits)

fruits.sort() # alphabetical  order
#fruits.clear() #makes list empty
print(fruits)