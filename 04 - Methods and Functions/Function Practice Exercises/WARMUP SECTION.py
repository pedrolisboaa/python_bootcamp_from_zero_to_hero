"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
but returns the greater if one or both numbers are odd
"""


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))
print(f'-------------------------')

"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
"""


def animal_crackers(text):
    array = text.split()
    if array[0][0].upper() == array[1][0].upper():
        return True
    return False


# Check
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print(f'-------------------------')

"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. 
If not, return False
"""


def makes_twenty(n1, n2):
    if int(n1) == 20 or int(n2) == 20 or int(n1 + n2) == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))
print(makes_twenty(30, 20))
print(makes_twenty(2, 3))
print(makes_twenty(2, 18))
