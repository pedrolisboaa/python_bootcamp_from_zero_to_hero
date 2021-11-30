try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError as e:
    print(e)

try:
    x = 5
    y = 0
    print(x / y)
except ZeroDivisionError:
    print(f'Não existe divisão por zero!')
finally:
    print(f'All done')


def ask():
    while True:
        try:
            n = int(input('Input an integer: '))
        except ValueError:
            print('An error occurred! Please try again!')
            continue
        else:
            print(f'Thank you, your number squared is: {n ** 2}')
            break


ask()
