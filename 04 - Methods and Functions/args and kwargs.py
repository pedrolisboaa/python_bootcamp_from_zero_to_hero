def myfunc(a, b):
    # return 5% of the sum of a and b
    return sum((a, b)) * 0.05


def my_func(*args):
    return sum(args) * 0.05


def myfunck(**kwargs):
    print(kwargs)


def nota(*args, **kwargs):
    soma = sum(args)
    return f'A nota de {kwargs["nome"]} é {soma}'


print(myfunc(40, 60))
print(my_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
myfunck(name='Pedro', sobrenome='Lisboa')
print(nota(5.5, 8.8, 10, nome='Pedro'))