# Test Python script for using classes to store animal info.

class Animal:
    '''
    A class used to encapsulate animal data of various species.
    '''
    count = 0 # number of animals recorded
    visits = 0 # number of visitors for each animal

    def __init__(self, name, cry):
        self.name = name
        self.cry = cry

        Animal.count += 1

    def details(self):
        return f"Animal chosen is {self.name}, which makes a noise of {self.cry}"

    def records(self):
        return f"{self.name} had {self.visits} visitors." # self.visits enables us to update number of visistors per animal

    @classmethod
    def from_string(cls, an_str):
        name, cry = an_str.split(" ")
        return cls(name, cry) # creates new animal

    @staticmethod
    def is_pet(animal):
        if animal == "Dog" or animal == "Cat":
            return True
        return False

print(Animal.__doc__)
print(f"Number of animals at beginning ==> {Animal.count}")
    
an1 = Animal("Cow", "Moo!")
an2 = Animal("Sheep", "Baah!")
an3 = Animal("Dog", "Woof!")
an4 = Animal("Cat", "Meow!")

an_str1 = "Cow Moo!"
an_str4 = "Cat Meow!"

new_an1 = Animal.from_string(an_str1) # creating an animal instance
new_an4 = Animal.from_string(an_str4)

print(new_an1.name)
print(new_an4.name)
print(f"Is {new_an1.name} a pet? {Animal.is_pet(new_an1.name)}")
print(f"Is {new_an4.name} a pet? {Animal.is_pet(new_an4.name)}\n")

print(f"Number of animals after assignations ==> {Animal.count}\n")

print(f"First animal is {an1.name}, {an1.cry}")
print(f"Using the class method... {an1.details()}\n")

print(an1.records())
print(an2.records())
an3.visits = 3
print(an3.records())
print(an4.records())