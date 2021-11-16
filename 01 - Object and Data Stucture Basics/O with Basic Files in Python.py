# my_file = open('test.txt')

# print(my_file.read())
# print('---------------------')


# my_file.seek(0)
# print(my_file.read())

# my_file.seek(0)
# contents = my_file.read()
#
# print(contents)
# print(contents)

# my_file.seek(0)
# print(my_file.readline())

# with open('test.txt') as my_test:
#     contents = my_test.read()
# #print(contents)
#
# with open('test.txt', 'r') as my_test:
#     print(my_test.read())
#
# with open('test.txt', 'a') as f:
#     f.write('\nPedro Lisboa')
#
# with open('test.txt', 'r') as my_test:
#     print(my_test.read())

with open('qwer.txt', 'w') as f:
    f.write('I create this file!')

with open('qwer.txt', 'r') as f:
    print(f.read())