t = (1, 2, 3, 4, 5, 6)
l = [1, 2, 3, 4, 5, 6]

print(type(t))
print(type(l))

print(len(t))
print(len(l))

new_tuple = t + ('a', 'a', 'a', 'b', 'c', 'd', 'e', 'e', 'e',)
print(new_tuple.count('a'))