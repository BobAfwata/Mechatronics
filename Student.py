#/usr/bin/env python 


# creating a class 

class Student:
    hobby = "Swimming " # attribute
    origin = "Kenya"

    # behavior of the student 
    def __init__(self ,name, id ,age , grade): 
        self.name = name
        self.id   = id 
        self.age  = age
        self.grade = grade

    def print_name(self,name):
        print(f"My name is {name}")

    def print_id(self,id):
        print(f"My Id is {id}")

    def display_age(self,age):
        return age
    
    def print_grade(self,grade):
        print(f"My grade was : {grade}")

# a copy of student / instance 
student1 = Student("Bob Afwata",629,29,"A")
student2 = Student("Moses Opuru",631,22,"B")
student3 = Student("Lesley Lelei",640,20,"A+")

print(student1.age)
print(student2.grade)
print(student3.name)

student2.print_id(789)

print(student3.display_age(45))
    # behaviour of the student 


class Teacher:

    def __init__(self ,name ,salary,subject): # constructor 
        self.name = name
        self.salary = salary 
        self.subject = subject 

    def increase_salary(self ,salary):
        new_salary = salary + (0.2 * salary)
        return new_salary 
    
    def print_salary(self,salary):
        print(f"The teacher earns : {salary} ksh ")


teacher1 = Teacher("Jada Elkasri",20000,"Biology")

teacher2 = Teacher("Emmanuel ",70000,"Physics")

print(teacher2.salary)
new_sal = teacher2.increase_salary(70000)
print(new_sal)
teacher2.print_salary(new_sal)