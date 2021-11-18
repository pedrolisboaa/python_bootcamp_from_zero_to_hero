def square(number):
    return number**2


my_list = [1, 2, 3, 4, 5, 6]
for i in map(square, my_list):
    print(i)

print(list(map(square, my_list)))