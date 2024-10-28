def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")

import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")

def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Test the generator
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")

def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")

# Exercise a)
#Modifying Iterative to Return List

def fibonacci_iterative_list(n):
    if n < 0:
        return []
    fib_list = [0] if n == 0 else [0, 1]
    for _ in range(2, n + 1):
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list
    
# Test the modified iterative function
print(fibonacci_iterative_list(10))

# Exercise b)

def first_fib_exceeding(value):
    if value < 0:
        return None 
    
    a, b = 0, 1
    index = 1
# Continue generating Fibonacci numbers until it exceed the given value 
    while b <= value:
        a, b = b, a + b
        index += 1

    return index

# Test the function with an example
value = 1000
index = first_fib_exceeding(value)
print(f"The index of the first Fibonacci number exceeding {value} is {index}.")

# Exercise c)

import math

def is_fibonacci(number):
    if number < 0:
        return False
    

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

    return is_perfect_square(5 * number * number + 4)

#Test the function
test_numbers = [0, 1, 2, 3, 4, 5, 13, 14, 21, 22]
for num in test_numbers:
    print(f"{num} is a Fibonacci number:{is_fibonacci(num)}")


# Exercise d)
def fibinacci_ratios(limit):
    a, b = 0, 1
    ratios = []

    for _ in range(2, limit + 1):
        ratio = b / a if a != 0 else None 
        ratios.append(ratio)
        a, b = b, a + b

    return ratios

#Test the function with a certain number of items
limit = 15
ratios = fibinacci_ratios(limit)
for i, ratio in enumerate(ratios, start=2):
    print(f"Ratio F{i}/F{i-1} = {ratios}")