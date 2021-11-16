"""
Use for, .split(), and if to create a Statement that will print out words that start with 's':
"""
st = 'Print only the words that start with s in this sentence'
text = st.split()
for p in text:
    if p[0] == 's' or p[0] == 'S':
        print(p)

print('*'*20)

"""
Use range() to print all the even numbers from 0 to 10.
"""
x = [x for x in range(11) if x % 2 == 0]
print(x)
print('*'*20)

"""
Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
"""

x = [x for x in range(51) if x % 3 == 0 and x > 0]
print(x)
print('*'*20)

"""
Go through the string below and if the length of a word is even print "even!"
"""
st = 'Print every word in this sentence that has an even number of letters'
text = st.split()
for p in text:
    if len(p) % 2 == 0:
        print(f'{p}: even')
    else:
        print(p)
print('*'*20)

"""
Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
"""
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i} - FizzBuzz')
    elif i % 3 == 0:
        print(f'{i} - Fizz ')
    elif i % 5 == 0:
        print(f'{i} - Buzz')

"""
Use List Comprehension to create a list of the first letters of every word in the string below:
"""
st = 'Create a list of the first letters of every word in this string'
print([x[0] for x in st.split()])