# =====================================================================
# EXCEPTION HANDLING IN PYTHON
# try, except, finally, Common Exceptions
# =====================================================================

# ---------------------------------------------------------------------
# 1. WHAT IS AN EXCEPTION?
# ---------------------------------------------------------------------
# An exception is an error that occurs during runtime of a program
# It interrupts the normal flow of the program

print("--- What is an Exception? ---")
print("Exceptions are errors that occur during program execution.")
print("They interrupt the normal flow of the program.\n")


# ---------------------------------------------------------------------
# 2. COMMON EXCEPTIONS
# ---------------------------------------------------------------------

print("--- Common Exceptions ---")

# ZeroDivisionError
print("1. ZeroDivisionError: Dividing by zero")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("   Error: Cannot divide by zero!\n")

# ValueError
print("2. ValueError: Invalid value for input")
try:
    age = int("abc")
except ValueError:
    print("   Error: Invalid literal for int()!\n")

# TypeError
print("3. TypeError: Wrong data type")
try:
    result = "5" + 3
except TypeError:
    print("   Error: Can only concatenate str to str!\n")

# NameError
print("4. NameError: Undefined variable")
try:
    print(undefined_variable)
except NameError:
    print("   Error: name 'undefined_variable' is not defined!\n")

# IndexError
print("5. IndexError: Invalid list index")
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("   Error: list index out of range!\n")

# KeyError
print("6. KeyError: Invalid dictionary key")
try:
    d = {"name": "Ram"}
    print(d["age"])
except KeyError:
    print("   Error: key 'age' not found!\n")

# FileNotFoundError
print("7. FileNotFoundError: File not found")
try:
    f = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("   Error: File not found!\n")


# ---------------------------------------------------------------------
# 3. TRY-EXCEPT BLOCK
# ---------------------------------------------------------------------

print("--- Try-Except Block ---")

# Basic try-except
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"100 / {num} = {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: That's not a valid number!")


# ---------------------------------------------------------------------
# 4. TRY-EXCEPT-FINALLY BLOCK
# ---------------------------------------------------------------------

print("\n--- Try-Except-Finally Block ---")

# finally always executes
try:
    num = int(input("Enter a number for finally block: "))
    result = 100 / num
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input!")
finally:
    print("This always executes (finally block)!")

print()


# ---------------------------------------------------------------------
# 5. MULTIPLE EXCEPT BLOCKS
# ---------------------------------------------------------------------

print("--- Multiple Except Blocks ---")

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter valid integers!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")


# ---------------------------------------------------------------------
# 6. CATCHING ALL EXCEPTIONS
# ---------------------------------------------------------------------

print("\n--- Catching All Exceptions ---")

try:
    # Some risky code
    lst = [1, 2, 3]
    print(lst[10])
    result = 10 / 0
except Exception as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")


# ---------------------------------------------------------------------
# 7. ELSE CLAUSE
# ---------------------------------------------------------------------

print("\n--- Else Clause ---")

# else executes if no exception occurs
try:
    num = int(input("Enter a positive number: "))
except ValueError:
    print("Error: Invalid input!")
else:
    print(f"You entered: {num}")
    if num > 0:
        print("That's a positive number!")
    else:
        print("That's not positive!")


# ---------------------------------------------------------------------
# 8. RAISE EXCEPTION
# ---------------------------------------------------------------------

print("\n--- Raise Exception ---")

def set_age(age):
    """Set age with validation."""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    print(f"Age set to: {age}")

try:
    set_age(25)
    set_age(-5)
except ValueError as e:
    print(f"Error: {e}")

try:
    set_age(200)
except ValueError as e:
    print(f"Error: {e}")


# ---------------------------------------------------------------------
# 9. CUSTOM EXCEPTIONS
# ---------------------------------------------------------------------

print("\n--- Custom Exceptions ---")

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}. Balance is {balance}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(1000)

try:
    print(f"Balance: {account.balance}")
    account.withdraw(500)
    print(f"After withdrawal: {account.balance}")
    account.withdraw(600)
except InsufficientFundsError as e:
    print(f"Error: {e}")


# ---------------------------------------------------------------------
# 10. PRACTICAL EXAMPLES
# ---------------------------------------------------------------------

print("\n--- Practical Examples ---")

# 1. Safe calculator
def safe_calculator():
    """Calculator with error handling."""
    try:
        num1 = float(input("\nEnter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        else:
            raise ValueError(f"Invalid operator: {op}")
        
        print(f"Result: {result}")
    
    except ValueError as e:
        print(f"Input Error: {e}")
    except ZeroDivisionError as e:
        print(f"Math Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# safe_calculator()  # Uncomment to run

# 2. Age validator
def validate_age(age_str):
    """Validate age input."""
    try:
        age = int(age_str)
    except ValueError:
        return False, "Age must be a number!"
    
    if age < 0:
        return False, "Age cannot be negative!"
    if age > 150:
        return False, "Age seems unrealistic!"
    
    return True, f"Valid age: {age}"

# Test cases
test_ages = ["25", "abc", "-5", "200", "0"]
for age in test_ages:
    valid, message = validate_age(age)
    print(f"Age '{age}': {message}")

print()

# 3. File handler with error handling
def read_file_safe(filename):
    """Read file with error handling."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return True, content
    except FileNotFoundError:
        return False, f"File '{filename}' not found!"
    except PermissionError:
        return False, f"Permission denied for '{filename}'!"
    except Exception as e:
        return False, f"Error reading file: {e}"

# Test
success, content = read_file_safe("test.txt")
if success:
    print(f"File content:\n{content}")
else:
    print(f"Error: {content}")

print()

# 4. List operations with error handling
def safe_list_operations():
    """List operations with error handling."""
    numbers = [10, 20, 30, 40, 50]
    
    try:
        index = int(input("Enter index (0-4): "))
        value = numbers[index]
        print(f"Value at index {index}: {value}")
    except IndexError:
        print(f"Error: Index must be between 0 and {len(numbers)-1}")
    except ValueError:
        print("Error: Please enter a valid integer!")

# safe_list_operations()  # Uncomment to run

# 5. User registration with validation
def register_user():
    """Register user with validation."""
    try:
        username = input("\nEnter username (min 3 chars): ")
        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters!")
        
        age = int(input("Enter age: "))
        if age < 13:
            raise ValueError("Must be at least 13 years old!")
        
        email = input("Enter email: ")
        if "@" not in email:
            raise ValueError("Invalid email format!")
        
        print(f"\nRegistration successful!")
        print(f"Username: {username}")
        print(f"Age: {age}")
        print(f"Email: {email}")
    
    except ValueError as e:
        print(f"Registration failed: {e}")

# register_user()  # Uncomment to run
