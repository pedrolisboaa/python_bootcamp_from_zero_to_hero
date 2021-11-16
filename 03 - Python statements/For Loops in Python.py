my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    print(num)

for num in my_list:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

list_sum = 0
for num in my_list:
    list_sum += num

print(list_sum)

for letter in 'Pedro Lisboa':
    print(letter.upper())

other_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
for a, b in other_list:
    print(a)
    print(b)


d = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}
for key, value in d.items():
    print(f'{key} - {value}')