from collections import Counter, defaultdict, namedtuple

# mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5]
# contador = Counter(mylist)
# print(contador)
# print(Counter('pasdapsldamisdmnimqomw'))
# print(Counter('Pedro Henrique do Nascimento Lisboa'))
# c = 'aaaaaaabbbbbbbbbccccccccddddddddddeeeeeeepppp'
# print(Counter(c))
# c2 = Counter(c)
# print(c2.most_common())


# d = defaultdict(lambda: 0)
# d['banana'] = 10
# print(d)
# print(d['pedro'])


Dog = namedtuple('Dog',['age', 'breed', 'name'])
sammy = Dog('10', 'Lab', 'Sammy')
print(sammy.name)
print(sammy.breed)
print(sammy.age)