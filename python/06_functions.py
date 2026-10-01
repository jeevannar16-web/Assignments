# =====================================================================
# FUNCTIONS IN PYTHON
# Built-in, User-defined, Parameters, Arguments, Recursion
# =====================================================================


# ---------------------------------------------------------------------
# 1. FUNCTION BASICS
# ---------------------------------------------------------------------
# A function is a block of reusable code that performs a specific task
# "Write once and call it whenever it is needed"

print("--- Function Basics ---")

# Without function (code duplication)
def without_function():
    num1 = 5
    print(num1 * num1)
    num2 = 10
    print(num2 * num2)
    num3 = 20
    print(num3 * num3)

# With function (reusable)
def square(number):
    """Returns the square of a number."""
    return number * number

print("Square of 5:", square(5))
print("Square of 10:", square(10))
print("Square of 20:", square(20))


# ---------------------------------------------------------------------
# 2. FUNCTION DEFINITION AND CALLING
# ---------------------------------------------------------------------

print("\n--- Function Definition and Calling ---")

def greet(name):
    """Greets a person by name."""
    print(f"Hello, {name}!")

greet("Ram")
greet("Shyam")

# Function with multiple parameters
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(10, 20)
print(f"10 + 20 = {result}")


# ---------------------------------------------------------------------
# 3. TYPES OF ARGUMENTS
# ---------------------------------------------------------------------

print("\n--- Types of Arguments ---")

# a. Positional Arguments
def full_name(first, last):
    return f"{first} {last}"

print(full_name("Ram", "Sharma"))  # Order matters

# b. Keyword Arguments
print(full_name(last="Sharma", first="Ram"))  # Order doesn't matter

# c. Default Arguments
def greet_with_age(name, age=18):
    """Greets with default age."""
    print(f"Hello {name}, you are {age} years old!")

greet_with_age("Hari")           # Uses default age
greet_with_age("Gita", 20)      # Uses provided age

# d. Required Arguments
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

print(f"10 / 2 = {divide(10, 2)}")


# ---------------------------------------------------------------------
# 4. *args AND **kwargs
# ---------------------------------------------------------------------

print("\n--- *args and **kwargs ---")

# *args - Variable number of positional arguments (stored as tuple)
def add_all(*args):
    """Adds all positional arguments."""
    print(f"args type: {type(args)}")
    print(f"args value: {args}")
    return sum(args)

print(f"Sum of 1,2,3: {add_all(1, 2, 3)}")
print(f"Sum of 1,2,3,4,5: {add_all(1, 2, 3, 4, 5)}")

# **kwargs - Variable number of keyword arguments (stored as dictionary)
def print_info(**kwargs):
    """Prints all keyword arguments."""
    print(f"kwargs type: {type(kwargs)}")
    print(f"kwargs value: {kwargs}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nStudent Info:")
print_info(name="Ram", age=20, city="Kathmandu", grade="A")

# Combining *args and **kwargs
def mixed_function(required, *args, **kwargs):
    """Function with required, *args, and **kwargs."""
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

mixed_function("Hello", 1, 2, 3, name="Ram", age=20)


# ---------------------------------------------------------------------
# 5. RETURN STATEMENT
# ---------------------------------------------------------------------

print("\n--- Return Statement ---")

# Function with return value
def add(a, b):
    return a + b

result = add(10, 20)
print(f"Add: {result}")

# Function without return value (returns None)
def greet(name):
    print(f"Hello, {name}!")

result = greet("World")
print(f"Return value: {result}")  # None

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {minimum}, Max: {maximum}")

# Early return
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")


# ---------------------------------------------------------------------
# 6. SCOPE OF VARIABLES
# ---------------------------------------------------------------------

print("\n--- Scope of Variables ---")

# Local scope
def my_function():
    local_var = "I am local"
    print(local_var)

my_function()
# print(local_var)  # Error: local_var is not defined

# Global scope
global_var = "I am global"

def show_global():
    print(global_var)

show_global()

# Using global keyword
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(f"Counter: {counter}")


# ---------------------------------------------------------------------
# 7. RECURSIVE FUNCTIONS
# ---------------------------------------------------------------------
# A function that calls itself

print("\n--- Recursive Functions ---")

# Factorial
def factorial(n):
    """Calculate factorial recursively."""
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 0: {factorial(0)}")

# Fibonacci
def fibonacci(n):
    """Return nth Fibonacci number."""
    if n <= 1:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

print(f"Fibonacci of 10: {fibonacci(10)}")

# Sum of digits
def sum_digits(n):
    """Sum of digits of a number."""
    if n == 0:  # Base case
        return 0
    return (n % 10) + sum_digits(n // 10)  # Recursive case

print(f"Sum of digits of 12345: {sum_digits(12345)}")

# Power calculation
def power(base, exp):
    """Calculate base^exp recursively."""
    if exp == 0:  # Base case
        return 1
    return base * power(base, exp - 1)  # Recursive case

print(f"2^10 = {power(2, 10)}")

# String reversal
def reverse_string(s):
    """Reverse a string recursively."""
    if len(s) <= 1:  # Base case
        return s
    return reverse_string(s[1:]) + s[0]  # Recursive case

print(f"Reverse of 'Python': {reverse_string('Python')}")


# ---------------------------------------------------------------------
# 8. LAMBDA FUNCTIONS
# ---------------------------------------------------------------------
# Small anonymous functions defined with lambda keyword

print("\n--- Lambda Functions ---")

# Basic lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
add = lambda a, b: a + b
print(f"Add 3 + 4: {add(3, 4)}")

# Lambda with if-else
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(f"7 is: {is_even(7)}")
print(f"8 is: {is_even(8)}")

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")

# Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# Lambda with sorted()
students = [("Ram", 20), ("Shyam", 18), ("Hari", 22)]
sorted_students = sorted(students, key=lambda x: x[1])
print(f"Sorted by age: {sorted_students}")


# ---------------------------------------------------------------------
# 9. BUILT-IN FUNCTIONS
# ---------------------------------------------------------------------

print("\n--- Built-in Functions ---")

# Math functions
print(f"abs(-5): {abs(-5)}")
print(f"round(3.7): {round(3.7)}")
print(f"max(1, 2, 3): {max(1, 2, 3)}")
print(f"min(1, 2, 3): {min(1, 2, 3)}")
print(f"sum([1, 2, 3]): {sum([1, 2, 3])}")
print(f"pow(2, 3): {pow(2, 3)}")

# String functions
print(f"len('Hello'): {len('Hello')}")
print(f"chr(65): {chr(65)}")
print(f"ord('A'): {ord('A')}")

# Type functions
print(f"isinstance(5, int): {isinstance(5, int)}")
print(f"type(5): {type(5)}")

# Sequence functions
print(f"range(5): {list(range(5))}")
print(f"enumerate(['a', 'b']): {list(enumerate(['a', 'b']))}")
print(f"zip([1, 2], ['a', 'b']): {list(zip([1, 2], ['a', 'b']))}")
print(f"reversed([1, 2, 3]): {list(reversed([1, 2, 3]))}")
print(f"sorted([3, 1, 2]): {sorted([3, 1, 2])}")


# ---------------------------------------------------------------------
# 10. PRACTICAL EXAMPLES
# ---------------------------------------------------------------------

print("\n--- Practical Examples ---")

# 1. Calculator with functions
def calculator():
    """Interactive calculator."""
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b
    
    num1 = float(input("\nEnter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = subtract(num1, num2)
    elif op == "*":
        result = multiply(num1, num2)
    elif op == "/":
        result = divide(num1, num2)
    else:
        result = "Invalid operator!"
    
    print(f"Result: {result}")

# calculator()  # Uncomment to run

# 2. Student grading system
def grade_student(name, marks):
    """Grade a student based on marks."""
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"
    
    return {"name": name, "marks": marks, "grade": grade}

students = [
    {"name": "Ram", "marks": 85},
    {"name": "Shyam", "marks": 45},
    {"name": "Hari", "marks": 92}
]

print("\nStudent Results:")
for student in students:
    result = grade_student(student["name"], student["marks"])
    print(f"{result['name']}: {result['marks']} marks -> Grade: {result['grade']}")

# 3. Prime number checker
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\nPrime numbers between 1 and 20:")
primes = [n for n in range(1, 21) if is_prime(n)]
print(primes)

# 4. Palindrome checker
def is_palindrome(s):
    """Check if a string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(f"\n'Racecar' is palindrome: {is_palindrome('Racecar')}")
print(f"'Hello' is palindrome: {is_palindrome('Hello')}")
