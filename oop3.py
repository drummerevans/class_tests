# Python OOP Tutorial 3: classmethods and staticmethods: https://www.youtube.com/watch?v=rq8cL2XMM5M  

#########################################################################
# PART 1

'''
Regular methods in a class automatically take instance as 1st arg == self
--> class as 1st arg? --> use classmethods
--> add a decorator --> @classmethod to change regular method to classmethod
'''

class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}" .format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
  
    '''
    Decorator alters functionality of method --> class 1st arg now
    cls == class variable name --> working with class instead of instance now
    '''
    @classmethod
    def set_raise_amt(cls, amount): 
        cls.raise_amt = amount


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

Employee.set_raise_amt(1.05) # automatically accepts class as 1st arg
# Employee.raise_amt = 1.05 # same as above
'''
Automatically accepts class: working with class now NOT instance
Could run classmethod from instances (e.g. emp_1.set_raise_amt(1.05))
--> doesn't make sense to do this though
'''

print(Employee.raise_amt) # class raise_amt
print(emp_1.raise_amt) # instance raise_amt
print(emp_2.raise_amt)

#########################################################################
# PART 2

'''
Use classmethods as alternative constructors
--> use classmethods to provide multiple ways of creating our objects
e.g. need employee info strings to be parsed (i.e. remove hythens)
'''

class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}" .format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
  
    @classmethod
    def set_raise_amt(cls, amount): 
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str): # convention -- use from_
        first, last, pay = emp_str.split("-") 
        return cls(first, last, pay) # creates new employee
        

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

'''
# first, last, pay = emp_str_1.split("-") 
# new_emp_1 = Employee(first, last, pay)

Don't want to parse strings (see above) for a new employee 
--> too much time wasted!
Create an alternative constructor to pass in string and create employee
'''

# parses string for us and creates new employee object easily
# classmethod as an alternative constructor
new_emp_1 = Employee.from_string(emp_str_1) 

print(new_emp_1.email)
print(new_emp_1.pay)

'''
Real world example: datetime module.
e.g. datatime(year, month, date)
@classmethod
def fromtimestamp(cls, t):
    y, m, d, hh, mm, ss, weekday, jday, dst = +time.localtime(t)
    return cls(y, m, d)
'''

#########################################################################
# PART 3

'''
regular methods automatically pass the instance as 1st arg ==> self
classmethods automatically pass the class as 1st arg ==> cls
staticmethods don't pass anything automatically
--> like regular functions but have some logical connection with the class

e.g. function to take in a date and return whether or not it's a work day
--> logical connection to Employee class
--> no dependence on instance or class variable
'''
# take a date and return if it's a work day

class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}" .format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
  
    @classmethod
    def set_raise_amt(cls, amount): 
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str): # convention -- use from_
        first, last, pay = emp_str.split("-") 
        return cls(first, last, pay) # creates new employee

    # TIP: if you don't use instance or class --> use staticmethod
    @staticmethod
    def is_workday(day):
        # INFO: 0 == Monday, ... 6 == Sunday
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

import datetime
my_date = datetime.date(2016, 7, 10) # args: year, month, day
print(Employee.is_workday(my_date))