#!/usr/bin/env python 

friends = ["Jada","Lesley","Moses","Emmanuel"]

for friend in friends:
    print(friend)


new_friends = ["Riak","Grace","John"]

friends.append("Bob") # 1 item at atime

friends.extend(new_friends)
#friends.append(["James", "Jack","Mercy"])

print(friends)

print(len(friends))

# list in a list

details = [["Age", "weight"] ,
           ["Korea","Kenya","Tanzania"] ,
           1,
           2,
           [4,8] ]

print(details[0][0])
print(details[0][1])
print(details[1][0])
print(details[1][2])
print(details[4][1])


#maxtrix multiplication
# [1 x 2 ]  * [2 x 2 ]