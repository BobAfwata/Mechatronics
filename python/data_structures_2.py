#!/usr/bin/env python

#arrays


# lists




# tuple
friends = ("Jada" ,"Lesley" ,"Moses", "Emmanuel")

print(friends)
numbers = tuple(range(10)) # 0 ....9
print(numbers)

print(len(friends))
print(friends[0])
print(friends[1])
print(friends[3])
#friends[1] = "Riak"

#friends.pop()  , extend() , append() # error cant pop in tuple : tuple is immutable

for friend in friends:
    print(friend)

# tuple --> list
print(type(friends))

friends_list = list(friends)
print(type(friends_list))

friends_list.append("Bob")
print(friends_list)

#list -->tuple

new_friends = tuple(friends_list)


# sets 

cities = {"Seoul" ,"Nairobi","Dodoma","Rabat"}

for city in cities:
    print(city)

#cities[0] = "Abu Dhabi"
#cities[1] = "Sanaa"
print(cities)

stuff = {"Bob" ,24, 24, 45.8, True} 

print(stuff)

stuff.remove("Bob")
print(stuff)

my_stuff = stuff.copy()

set_numbers = {1,2,3,4}

print(set_numbers)
set_numbers.add(5)
set_numbers.update({6,7,8})
print(set_numbers)

set_numbers.clear() #deletes everything

print(set_numbers)


# dictionaries 
# special type of set stores data in key:value pairs 

car = {"brand" : "Toyota" ,"model":"Land Cruiser" ,"year" :2024 ,"fuel_cc" : 2900}

print(car["brand"]) #prints the value
print(car["fuel_cc"])

# use for loop to print all the keys  dict = {key : value}
print("-----------------------------")
for key in car:
    print(key)

print("-----------------------------")

for val in car.values():
    print(val)

del(car["brand"]) 
new_car = car.copy()


print(new_car)