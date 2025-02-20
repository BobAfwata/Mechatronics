#!/usr/bin/env python

# list of fruits 
#mutable - size / content
fruits = ["Lemon", "Orange","Apple","Kiwi","Peaches","Mangoes","Guavas"] #string


print(fruits) 
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
fruits.pop()
print(fruits)
fruits.pop()
print(fruits)


fruits.insert(3,"Pawpaw")

fruits.extend(["Tomatoes","Cherry","Grapes"])
print(fruits)

#fruits.sort()
#fruits.clear()
#print(fruits)