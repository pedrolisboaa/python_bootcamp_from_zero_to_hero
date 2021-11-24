class Animal:
    def __init__(self):
        print('ANIMAL CREATED')

    def who_i_am(self):
        print(f'I am an animal')

    def eat(self):
        print('I am eating')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('DOG CREATED')

    def who_i_am(self):
        print('I am a dog!')

    def eat(self):
        print(f'I am dog and eating')

    def bark(self):
        print('WOOF')


if __name__ == '__main__':
    a = Animal()
    a.eat()
    a.who_i_am()

    d = Dog()
    d.eat()
    d.who_i_am()
    d.eat()
    d.bark()