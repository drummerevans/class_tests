# Script for generating a test class and instances.

class Calculator:
    '''A class for performing arithmetic operations.'''
    class_atr = 0 # class attribute == Python variable that belongs to class - outside of __init__ function
    add_count = 0
    def __init__(self, num1, num2):
        self.inst_atr = 0 # instance attribute == Python variable belonging to only one object - inside __init__ function
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        self.inst_atr += 1
        self.add_count += 1
        return "Adding, {} and {} we get {}" .format(self.num1, self.num2, self.num1 + self.num2)
    
    def subtraction(self):
        self.inst_atr += 1
        return "Subtracting, {} and {} we get {}" .format(self.num1, self.num2, self.num1 - self.num2)

    def multiplication(self):
        self.inst_atr += 1
        return "Multiplying, {} and {} we get {}" .format(self.num1, self.num2, self.num1 * self.num2)

    def division(self):
        self.inst_atr += 1
        return "Dividing, {} and {} we get {}" .format(self.num1, self.num2, self.num1 / self.num2)

test1 = Calculator(4, 4)
test2 = Calculator(2, 2)

print(test1.num1) # printing instance attributes
print(test1.num2)

print(test1.add_count)

print("Result by {}; instance attribute count = {}" .format(test1.addition(), test1.inst_atr))
print("Result by {}; instance attribute count = {}" .format(test1.subtraction(), test1.inst_atr))
print("Result by {}; instance attribute count = {}" .format(test1.multiplication(), test1.inst_atr))
print("Result by {}; instance attribute count = {}" .format(test1.division(), test1.inst_atr))

print(test1.add_count)

print("Result by {}; instance attribute count = {}" .format(test1.addition(), test1.inst_atr))

print(test1.add_count)
