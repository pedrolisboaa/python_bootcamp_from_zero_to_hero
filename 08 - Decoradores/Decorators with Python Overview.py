def hello(name='Pedro'):
    print('The hello() functions has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is the welcome() inside hello!'

    print(greet())
    print(welcome())
    print('End of the hello function')


hello()