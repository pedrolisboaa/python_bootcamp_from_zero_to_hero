for num in range(3, 10, 2):
    print(num)

lista = list(range(30))
print(lista)

name = 'peter'
for index, letter in enumerate(name):
    print(f'{index}: {letter}')


# ZIP
mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c', 'd', 'e']
mylist3 = []
mylist4 = [100, 200, 300, 400, 500]
for item in zip(mylist1, mylist2,  mylist4):
    mylist3.append(item)

print(mylist3)

mylist5 = list(zip(mylist1,  mylist2, mylist4))
print(mylist5)