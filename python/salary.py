#!/usr/bin/env python
# challange  
# wap that does the following
# earn less than 50,000 get 10% salary increase 
# earn btn 50,000 --100,000 get 5 % increase 
# earn more than 100,000 get 2% tax
#display new salary

salary = int(input("Enter your current salary :"))

if salary < 50000 :
    new_salary = salary *1.1 
elif salary >= 50000 or salary <= 100000:
    new_salary = salary * 1.05 
elif salary > 100000:
    new_salary = salary * 0.98
else :
    print(" You are not affected ")

print(new_salary)