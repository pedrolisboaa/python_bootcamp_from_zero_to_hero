def even_check(number):
    if number % 2 == 0:
        return 'Even'
    return 'Odd'


result_1 = even_check(10)
result_2 = even_check(23)
print(result_1)
print(result_2)


def check_even_list(num_list):
    for n in num_list:
        if n % 2 == 0:
            return 'Exist Even'
    return "Don't exist even in list"


result_list = check_even_list([1, 3, 5])
print(result_list)