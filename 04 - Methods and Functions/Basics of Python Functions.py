def say_hello():
    print('hello')


def say_hello_name(name='Default'):
    print(f'Hello {name}')


def add_num(num1, num2):
    return num1 + num2


say_hello()
say_hello_name('Pedro')
say_hello_name()
result = add_num(5, 6)
print(result)