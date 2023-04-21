class Arithmetic():
    ''' A base class for containing useful Arithmetic functions. '''
    def __init__(self, my_list):
        self.my_list = my_list

    def addition(self, my_list):
        holder = 0
        for num in self.my_list:
            holder += num
        return holder

list1 = [1, 2, 3, 4, 5]
test1 = Arithmetic(list1)
print("The input list is: ", test1.my_list)
print(test1.addition(list1))

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.can_drink = age > 18

    @staticmethod
    def shout_loudly():
        print('hello!!!!')

B = Person('B', 29)
T = Person('T', 25)
Freddie = Person('Freddie!!!', 8) # he was drunk when filling this out
Person.shout_loudly()

people = [B, T, Freddie]
who_is_going_to_the_pub = [i.name for i in people if i.can_drink]
print(who_is_going_to_the_pub)

for i in people:
    if i.can_drink:
        print(i.name)