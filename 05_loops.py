# =====================================================================
# LOOPS IN PYTHON
# for loop, while loop, range(), break, continue, pass
# =====================================================================

# ---------------------------------------------------------------------
# 1. THE range() FUNCTION
# ---------------------------------------------------------------------
# Generates a sequence of numbers

print("--- range() Function ---")

# range(stop) - starts from 0, stops before 'stop'
print("range(5):", list(range(5)))

# range(start, stop) - starts from 'start', stops before 'stop'
print("range(2, 8):", list(range(2, 8)))

# range(start, stop, step) - with step size
print("range(1, 10, 2):", list(range(1, 10, 2)))  # Odd numbers
print("range(10, 0, -1):", list(range(10, 0, -1)))  # Countdown


# ---------------------------------------------------------------------
# 2. THE for LOOP
# ---------------------------------------------------------------------
# Most commonly used loop, executes for a fixed number of iterations

print("\n--- The for Loop ---")

# Basic for loop
print("Numbers 0 to 4:")
for i in range(5):
    print(i, end=" ")
print("\n")

# For loop with step
print("Even numbers 0 to 10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print("\n")

# For loop with list
print("\nLooping through a list:")
fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
    print(f"  - {fruit}")

# For loop with string
print("\nLooping through a string:")
name = "Python"
for char in name:
    print(char, end=" ")
print("\n")

# For loop with tuple
print("\nLooping through a tuple:")
colors = ("Red", "Green", "Blue")
for color in colors:
    print(f"  - {color}")

# For loop with dictionary
print("\nLooping through a dictionary:")
student = {"name": "Ram", "age": 20, "city": "Kathmandu"}
for key, value in student.items():
    print(f"  {key}: {value}")

# Using enumerate (index + value)
print("\nUsing enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")


# ---------------------------------------------------------------------
# 3. THE while LOOP
# ---------------------------------------------------------------------
# Executes as long as condition is True

print("\n--- The while Loop ---")

# Basic while loop
print("Countdown:")
i = 5
while i > 0:
    print(i, end=" ")
    i -= 1
print("Go!\n")

# While loop for sum
print("Sum of numbers 1 to 10:")
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(f"Total: {total}\n")

# While loop with user input
print("--- Guess the Number Game ---")
secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it!")


# ---------------------------------------------------------------------
# 4. BREAK STATEMENT
# ---------------------------------------------------------------------
# Terminates the loop immediately

print("\n--- Break Statement ---")

print("Numbers 1 to 10, stop at 7:")
for i in range(1, 11):
    if i == 7:
        print("\nFound 7! Breaking the loop.")
        break
    print(i, end=" ")
print("\n")

# Finding first even number
numbers = [1, 3, 5, 8, 9, 10, 11]
print(f"\nFirst even number in {numbers}:")
for num in numbers:
    if num % 2 == 0:
        print(f"Found: {num}")
        break


# ---------------------------------------------------------------------
# 5. CONTINUE STATEMENT
# ---------------------------------------------------------------------
# Skips current iteration and continues with next

print("\n--- Continue Statement ---")

print("Odd numbers 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=" ")
print("\n")

# Skip specific value
print("\nSkip 'Banana' in fruits:")
fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
    if fruit == "Banana":
        continue
    print(f"  - {fruit}")


# ---------------------------------------------------------------------
# 6. PASS STATEMENT
# ---------------------------------------------------------------------
# Placeholder that does nothing

print("\n--- Pass Statement ---")

# Using pass as placeholder
for i in range(5):
    if i == 3:
        pass  # Will implement later
    print(i, end=" ")
print("\n")

# Empty function (will add implementation later)
def empty_function():
    pass


# ---------------------------------------------------------------------
# 7. NESTED LOOPS
# ---------------------------------------------------------------------
# Loop inside another loop

print("\n--- Nested Loops ---")

# Multiplication table
print("Multiplication Table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()

print()

# Pattern printing
print("Star Pattern:")
size = 5
for i in range(size):
    for j in range(i + 1):
        print("*", end=" ")
    print()

print()

# X pattern
print("X Pattern:")
size = 5
for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# ---------------------------------------------------------------------
# 8. LOOP ELSE CLAUSE
# ---------------------------------------------------------------------
# Executes when loop completes normally (without break)

print("\n--- Loop Else Clause ---")

# Find prime number
num = 11
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print(f"{num} is not prime (divisible by {i})")
        break
else:
    print(f"{num} is a prime number!")


# ---------------------------------------------------------------------
# 9. PRACTICAL EXAMPLES
# ---------------------------------------------------------------------

print("\n--- Practical Examples ---")

# 1. Factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = 5
print(f"Factorial of {num}: {factorial(num)}")

# 2. Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

fibonacci(10)

# 3. Sum of list elements with error handling
def sum_list(numbers):
    total = 0
    try:
        for num in numbers:
            total += num
    except TypeError:
        return "Error: List contains non-numeric values"
    return total

print(f"\nSum of [1, 2, 3, 4, 5]: {sum_list([1, 2, 3, 4, 5])}")

# 4. Count even numbers in tuple
def count_even(tup):
    count = 0
    for num in tup:
        if num % 2 == 0:
            count += 1
    return count

numbers = (1, 2, 3, 4, 5, 6, 7, 8)
print(f"Even numbers in {numbers}: {count_even(numbers)}")

# 5. Find greatest number in list
def find_greatest(lst):
    if not lst:
        return None
    greatest = lst[0]
    for num in lst:
        if num > greatest:
            greatest = num
    return greatest

numbers = [23, 45, 12, 67, 34, 89, 56]
print(f"Greatest in {numbers}: {find_greatest(numbers)}")

# 6. Find highest occurring number
def highest_occurring(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    max_count = 0
    max_num = lst[0]
    for num, count in freq.items():
        if count > max_count:
            max_count = count
            max_num = num
    return max_num, max_count

numbers = [1, 2, 3, 2, 4, 2, 5, 3, 2]
num, count = highest_occurring(numbers)
print(f"Highest occurring: {num} (appears {count} times)")

# 7. While loop - Digital root
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

print(f"Digital root of 942: {digital_root(942)}")

# 8. Nested loop - Matrix multiplication
def matrix_multiply(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    
    if cols_a != rows_b:
        return "Cannot multiply"
    
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(f"\nMatrix A: {A}")
print(f"Matrix B: {B}")
print(f"A x B: {matrix_multiply(A, B)}")
