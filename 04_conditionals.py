# =====================================================================
# CONDITIONAL STATEMENTS IN PYTHON
# if, if-else, if-elif-else, nested if
# =====================================================================

# ---------------------------------------------------------------------
# 1. THE if STATEMENT
# ---------------------------------------------------------------------
# Executes code block when condition is True

print("--- The if Statement ---")
age = 18

if age >= 18:
    print("You are eligible to vote!")
    print("Welcome to democracy!")

print("This prints regardless of the condition.\n")


# ---------------------------------------------------------------------
# 2. THE if-else STATEMENT
# ---------------------------------------------------------------------
# Chooses between two possible outcomes

print("--- The if-else Statement ---")
marks = 45

if marks >= 50:
    print("Congratulations! You passed!")
else:
    print("Sorry, you failed. Better luck next time!")

print()

# Another example
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

print()


# ---------------------------------------------------------------------
# 3. THE if-elif-else STATEMENT
# ---------------------------------------------------------------------
# Used when there are multiple conditions to check

print("--- The if-elif-else Statement ---")
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")

print()

# Temperature example
temperature = float(input("Enter temperature in Celsius: "))

if temperature > 40:
    print("It's extremely hot! Stay indoors!")
elif temperature > 30:
    print("It's hot outside. Wear light clothes!")
elif temperature > 20:
    print("It's pleasant weather!")
elif temperature > 10:
    print("It's a bit cold. Wear a jacket!")
else:
    print("It's freezing! Stay warm!")

print()


# ---------------------------------------------------------------------
# 4. NESTED IF STATEMENT
# ---------------------------------------------------------------------
# An if statement inside another if statement

print("--- Nested if Statement ---")
age = 25
has_license = True

if age >= 18:
    print("You are eligible for a license.")
    if has_license:
        print("You can drive!")
    else:
        print("You need to get a license first.")
else:
    print("You are too young to get a license.")

print()

# Nested if with elif
num = 15
if num > 0:
    print("Number is positive.")
    if num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
    if num % 3 == 0:
        print("Number is divisible by 3.")
else:
    print("Number is not positive.")

print()


# ---------------------------------------------------------------------
# 5. TERNARY OPERATOR (Short Hand if-else)
# ---------------------------------------------------------------------

print("--- Ternary Operator ---")
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")

num = 10
result = "Positive" if num > 0 else ("Zero" if num == 0 else "Negative")
print(f"Number: {num}, Result: {result}")

print()


# ---------------------------------------------------------------------
# 6. LOGICAL OPERATORS IN CONDITIONS
# ---------------------------------------------------------------------

print("--- Logical Operators ---")
age = 25
income = 50000

# AND - Both conditions must be True
if age >= 18 and income >= 30000:
    print("Loan approved (AND condition met)!")

# OR - At least one condition must be True
if age < 18 or income < 30000:
    print("Loan rejected (OR condition met)!")
else:
    print("Loan processing...")

# NOT - Reverses the boolean value
is_student = False
if not is_student:
    print("You need to pay full price.")

print()


# ---------------------------------------------------------------------
# 7. PRACTICAL EXAMPLES
# ---------------------------------------------------------------------

print("--- Practical Examples ---")

# Example 1: ATM Cash Withdrawal System
print("\n--- ATM Cash Withdrawal System ---")
balance = 10000
print(f"Current Balance: Rs. {balance}")

amount = int(input("Enter amount to withdraw: "))

if amount <= 0:
    print("Invalid amount!")
elif amount > balance:
    print("Insufficient balance!")
else:
    balance -= amount
    print(f"Withdrawal successful!")
    print(f"Remaining balance: Rs. {balance}")

print()

# Example 2: Simple Calculator
print("--- Simple Calculator ---")
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
else:
    result = "Invalid operator!"

print(f"Result: {result}")

print()

# Example 3: Leap Year Check
print("--- Leap Year Check ---")
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year!")
    else:
        print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")

print()

# Example 4: BMI Calculator
print("--- BMI Calculator ---")
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

print()

# Example 5: Voting Eligibility
print("--- Voting Eligibility ---")
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age!")
elif age < 18:
    print(f"You are {age} years old. You cannot vote yet.")
    print(f"You need to wait {18 - age} more years.")
else:
    print(f"You are {age} years old. You are eligible to vote!")
