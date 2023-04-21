# Python OOP Tutorial 1: Classes and Instances: https://www.youtube.com/watch?v=ZDa-Z5JzLYM 

'''
Data and functions assocaited with class 
--> attributes and methods, resepectively
'''

#########################################################################
# PART 1

class Employee:
    pass

'''
Class = blueprint for creating instances
Each employee = instance of the class
'''

# unique instances of the Employee class
emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)

# instance variables contain data that is unique to each instance
# setting employee information manually - takes time!

emp_1.first = "Corey"
emp_1.last = "Schafer"
emp_1.email = "Corey.Schafer@company.com"
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "Test.User@company.com"
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

#########################################################################
# PART 2

class Employee:
    '''
    initialise method or constructor
    methods in class receive the instance as the 1st arg automatically
    --> call the instance self, by convention
    '''
    def __init__(self, first, last, pay):
        # set all instance variables
        self.first = first # same as emp_1.first = "Corey", for example
        # could use self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

'''
instance passed automatically (but not received automatically in Class)
--> leave out self
--> only need to provide name and pay, below
'''
emp_1 = Employee("Corey", "Schafer", 50000) # emp_1 passed as self
emp_2 = Employee("Test", "User", 60000) # emp_2 passed as self

print(emp_1.email)
print(emp_2.email)

#########################################################################
# PART 3

print("{} {}".format(emp_1.first, emp_1.last))

'''
lots to type!
--> create a method in class to print name!
'''

class Employee:

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return "{} {} ".format(self.first, self.last)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)
print(emp_1.fullname())

'''
need parenthesis for methods
Behind the scene, in every instance method call,
Python sends the instances also with that method call
--> emp_1.fullname() == Employee.fullname(emp_1)
'''

print(Employee.fullname(emp_1)) # passes in emp_1 as self here --> that's why we need self in Class
