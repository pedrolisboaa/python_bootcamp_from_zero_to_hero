from math import pi
class Dog:
    # CLASS OBJECT ATTRIBUTE
    # Same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self, number):
        print(f'WOOF! My name is {self.name.capitalize()} and my number is {number}')


class Circle:
    # Class object attribute
    PI = pi

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumference(self):
        print(self.radius * self.PI * 2)

if __name__ == '__main__':

    my_dog = Dog('lab', 'sammy')
    print(my_dog.species)
    print(my_dog.name)
    print(my_dog.breed)
    my_dog.bark(9995555)

    my_circle = Circle(30)
    my_circle.get_circumference()