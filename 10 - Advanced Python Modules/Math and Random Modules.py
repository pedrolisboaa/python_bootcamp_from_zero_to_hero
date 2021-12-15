import math
import random
from math import pi


# value = 4.35
# print(math.floor(value))
# print(math.ceil(value))
# print(pi)
# print(math.log(100, 10))
# print(random.randint(0, 100))

#random.seed(101)
print(random.randint(0, 100))
print(random.randint(0, 100))

my_list = list(range(20))
print(my_list)

print(random.choice(my_list))

# repitindo números
print(random.choices(my_list, k=10))

# sem repetição
print(random.sample(my_list, k=10))