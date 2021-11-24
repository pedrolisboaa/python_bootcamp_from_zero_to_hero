class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')


class Dog(Animal):

    def speak(self):
        return self.name + ' says woof!'


class Cat(Animal):

    def speak(self):
        return self.name + ' says meow!'


if __name__ == '__main__':
    niko = Dog('Niko')
    sam = Cat('Sam')

    print(niko.speak())
    print(sam.speak())