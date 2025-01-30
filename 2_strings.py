#!/usr/bin/env python

f_name = "Bob"
s_name = "Afwata"

full_name = f_name + "  " + s_name

print("My full name is " ,full_name)

#string operations 

#.upper() convert lower case strings  to upper cases 

name = "bob"
print(name.upper())

#.lower() convert upper case strings  to lower cases 

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



