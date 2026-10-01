# =====================================================================
# PYTHON PROGRAMMING FUNDAMENTALS
# Variables, Data Types, Operators, Input
# =====================================================================

# ---------------------------------------------------------------------
# 1. PRINT FUNCTION
# ---------------------------------------------------------------------

print("Hello, World!")
print("Welcome to Python Programming!")

# Printing multiple values
name = "Bigyesh"
age = 26
print("Name:", name, "Age:", age)

# Using end parameter (print on same line)
print("Hello", end=" ")
print("World")

# Using sep parameter (separator between values)
print("Python", "Java", "C++", sep=", ")


# ---------------------------------------------------------------------
# 2. DATA TYPES IN PYTHON
# ---------------------------------------------------------------------

# Integer - Whole numbers
x = 10
y = -5
print(f"Integer: {x}, type: {type(x)}")

# Float - Decimal numbers
price = 9.99
temperature = -3.5
print(f"Float: {price}, type: {type(price)}")

# String - Text data
name = "Python"
greeting = 'Hello'
print(f"String: {name}, type: {type(name)}")

# Boolean - True/False values
is_active = True
is_admin = False
print(f"Boolean: {is_active}, type: {type(is_active)}")


# ---------------------------------------------------------------------
# 3. VARIABLES AND NAMING RULES
# ---------------------------------------------------------------------

# Valid variable names
my_variable = 10
_private = 20
camelCase = 30
name1 = "Alice"
MAX_SIZE = 100

# Invalid variable names (these would cause errors if uncommented)
# 2name = "error"        # Cannot start with digit
# my variable = "error"  # Cannot have spaces
# my-var = "error"       # Cannot have hyphens
# @name = "error"        # Cannot use special characters

# Multiple variable declaration
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# Same value to multiple variables
x = y = z = 0
print(f"x={x}, y={y}, z={z}")

# Variable reassignment
num = 10
print(f"num = {num}")
num = 20
print(f"num = {num}")

# Case sensitive
Name = "Alice"
name = "Bob"
print(f"Name = {Name}, name = {name}")


# ---------------------------------------------------------------------
# 4. TYPE CONVERSION AND TYPE CHECKING
# ---------------------------------------------------------------------

# Type conversion
age_str = "25"
age_int = int(age_str)       # String to Integer
price_float = float("19.99") # String to Float
num_str = str(100)           # Integer to String

print(f"String to Int: {age_int}, type: {type(age_int)}")
print(f"String to Float: {price_float}, type: {type(price_float)}")
print(f"Int to String: {num_str}, type: {type(num_str)}")

# Boolean conversion
print(bool(1))      # True
print(bool(0))      # False
print(bool("Hi"))   # True
print(bool(""))     # False


# ---------------------------------------------------------------------
# 5. OPERATORS IN PYTHON
# ---------------------------------------------------------------------

a = 15
b = 4

# Arithmetic Operators
print("--- Arithmetic Operators ---")
print(f"{a} + {b} = {a + b}")    # Addition
print(f"{a} - {b} = {a - b}")    # Subtraction
print(f"{a} * {b} = {a * b}")    # Multiplication
print(f"{a} / {b} = {a / b}")    # Division
print(f"{a} // {b} = {a // b}")  # Floor Division
print(f"{a} % {b} = {a % b}")    # Modulus (Remainder)
print(f"{a} ** {b} = {a ** b}")  # Exponentiation

# Assignment Operators
print("\n--- Assignment Operators ---")
x = 10
print(f"x = {x}")
x += 5   # x = x + 5
print(f"x += 5 -> {x}")
x -= 3   # x = x - 3
print(f"x -= 3 -> {x}")
x *= 2   # x = x * 2
print(f"x *= 2 -> {x}")
x /= 4   # x = x / 4
print(f"x /= 4 -> {x}")

# Comparison Operators
print("\n--- Comparison Operators ---")
print(f"{a} == {b}: {a == b}")   # Equal to
print(f"{a} != {b}: {a != b}")   # Not equal to
print(f"{a} > {b}: {a > b}")     # Greater than
print(f"{a} < {b}: {a < b}")     # Less than
print(f"{a} >= {b}: {a >= b}")   # Greater than or equal to
print(f"{a} <= {b}: {a <= b}")   # Less than or equal to

# Logical Operators
print("\n--- Logical Operators ---")
x = True
y = False
print(f"True AND False: {x and y}")
print(f"True OR False: {x or y}")
print(f"NOT True: {not x}")

# Membership Operators
print("\n--- Membership Operators ---")
fruits = ["Apple", "Banana", "Orange"]
print(f"'Apple' in fruits: {'Apple' in fruits}")
print(f"'Grape' not in fruits: {'Grape' not in fruits}")


# ---------------------------------------------------------------------
# 6. INPUT FUNCTION
# ---------------------------------------------------------------------

print("\n--- Input Function ---")

# Taking input from user
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Type casting is required for numbers
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")

# Calculator using input
print("\n--- Simple Calculator ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
if num2 != 0:
    print(f"Division: {num1 / num2}")
else:
    print("Cannot divide by zero!")
