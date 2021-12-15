def func_one(n):
    return [str(num) for num in range(n)]


def func_two(n):
    return list(map(str, range(n)))


import time

# Current time before
start_time = time.time()
# Run CODE
result = func_one(10)
# Current time after running code
end_time = time.time()
# Elapsed time
elapsed_time = end_time - start_time

print(elapsed_time)

# Current time before
start_time = time.time()
# Run CODE
result2 = func_two(10)
# Current time after running code
end_time = time.time()
# Elapsed time
elapsed_time = end_time - start_time

print(elapsed_time)

import timeit
stmt = """
func_one(100)
"""

setup = """
return [str(num) for num in range(n)]
"""

print(timeit.timeit(stmt, setup, number=10000))