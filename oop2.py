# Python OOP Tutorial 2: Class Variables: https://www.youtube.com/watch?v=BJ-VvGyQxho 

#########################################################################
# PART 1

class Employee:
    # class variables are the same for each instance

    def __init__(self, first, last, pay):
        # instance vars == data that are used for data unique to each instance
        # all the variables below are instance variables  
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}" .format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# emp_1.raise_amount
# Employee.raise_amount

#########################################################################
# PART 2

'''
Would be nice to access raise amount, e.g. emp_1.raise_amount
--> Need to easily update raise amount - hidden in method!
--> not easy to access and update!
--> Use a class variable to easily change this, in multiple locations at once
'''

class Employee:
    
    raise_amount = 1.04 # class variable 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}" .format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

'''
Class variable can be accessed from class itself and both instances of class.
class variables accessed via instance???

When we try to access attribute on instance...
--> it will first check if instance contains that attribute
--> if it doesn't, it will check if class contains that attribute

--> e.g. emp_1.raise_amount doesn't actually have raise_amount
--> accessing class' raise_amount attribute - see prints below
'''

print(emp_1.__dict__)  # no raise_amount in printed list

print(Employee.__dict__) 
'''
class DOES contain raise_amount attribute 
--> that's the value the instances see when we access raise_amount value from instances
'''

#########################################################################
# PART 3

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        # Employee. here because constant class value updated && can be overriden per instance if needed
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}" .format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount) # changes all instances amount
        self.pay = int(self.pay * self.raise_amount) # lets us change amount for single instance

print(Employee.num_of_emps)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(Employee.num_of_emps)

# Employee.raise_amount = 1.05 # raise_amount changed for class and ALL instances

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

emp_1.raise_amount = 1.05 
'''
only changes raise_amount for emp_1
assignment above created raise_amount attribute within emp_1 - see print below
'''
print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount) 
print(emp_2.raise_amount)