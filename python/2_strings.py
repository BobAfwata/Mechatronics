#!/usr/bin/env python

f_name = "Bob"
s_name = "Afwata"

full_name = f_name + "  " + s_name

print("My full name is " ,full_name)

print("My full name is  {}".format(full_name))



print(f"My full name is {full_name}")

print("My full name is  %s ".format(full_name))

print("Hello \\ world")
print("\'A man is born to suffer\' - Bob Afwata 2025 ")
print("\"A man is born to suffer\" - Bob Afwata 2025 ")
print("\a")

print(" I am {0} and I come from {1}" .format("Bob" , "Kenya"))
print(" I am {name} and I come from {country}" .format( name ="Bob" , country = "Kenya"))

print("My average of this {0} was {1:.2f}%    {2:.3f}%".format("semester", 78.234876,25.9099))


#string operations 

#.upper() convert lower case strings  to upper case 

name = "bob"
print(name.upper())

#.lower() convert upper case strings  to lower case 

name = "BOB"
print(name.lower())

city = "eldoret" # 7 characters in the string eldoret
print(len(city))

print(city.startswith('f'))
print(city.endswith('t'))

sentence = "I am 24 years old "

new_sentence = sentence.replace("24","30") 
print(new_sentence)

print(sentence.isalpha()) # have alphanumeric characters without space

#find(char / string)

print(sentence.find("a"))
print(sentence.find("ears"))

print(sentence.count('r'))

hobby = "football"

new_hobby = hobby.split('t')
print(new_hobby)
print(hobby.capitalize())



