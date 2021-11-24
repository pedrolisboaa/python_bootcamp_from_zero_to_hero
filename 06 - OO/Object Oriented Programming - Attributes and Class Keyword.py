class Dog:
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots


if __name__ == '__main__':
    my_dog = Dog('Lab', 'Sammy', False)
    print(my_dog.breed)
    print(my_dog.name)
    print(my_dog.spots)