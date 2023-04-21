class MyClass:
    x = 5
    y = x * 2

p1 = MyClass()
print(p1.x)
print(p1.y)

class Car():
    ''' A base class for all motor vehicle properties. '''
    # assigns values to object properties e.g. make to self.make, or other operations that are necessary to do when the object is being created
    counter = 0
    # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
    def __init__(self, make, colour): 
        self.make = make
        self.colour = colour
        Car.counter += 1

    def number(self):
        print("This is a {:s} model of car with colour {:s} at position {:d}" .format(self.make, self.colour, Car.counter))
        return Car.counter

car1 = Car("Ford", "Red")
print("At number {:d} we have a car that is a {:s} {:s}" .format(car1.counter, car1.make, car1.colour))
car1.number() # calling the method inside the car1 instance of the class Car

car2 = Car("Ford", "Green")
print("At number {:d} we have a car that is a " .format(car2.counter), car2.make, car2.colour)
car2.number()


