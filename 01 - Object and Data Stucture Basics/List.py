my_list = [1, 2, 3]
print(my_list[1::])
another_list = ['Peter', 'Josh', 'Mett', 'Sam']

print(my_list + another_list)

new_list = my_list + another_list
print(new_list)

new_list[0] = 'FISH'
print(new_list)

new_list.pop()
print(new_list)

pop_item = new_list.pop(0)
print(new_list)
print(pop_item)

list_alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
list_alphabet.sort()
print(list_alphabet)
list_alphabet.reverse()
print(list_alphabet)