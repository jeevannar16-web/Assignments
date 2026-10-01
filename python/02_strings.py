# =====================================================================
# STRINGS IN PYTHON
# Indexing, Slicing, Methods, f-strings
# =====================================================================

# ---------------------------------------------------------------------
# 1. STRING BASICS
# ---------------------------------------------------------------------

# Strings can be created with single or double quotes
name = "Bigyesh"
greeting = 'Hello World'
multiline = """This is a
multiline string"""

print(f"Name: {name}")
print(f"Greeting: {greeting}")
print(f"Multiline:\n{multiline}")


# ---------------------------------------------------------------------
# 2. STRING INDEXING (Zero-based)
# ---------------------------------------------------------------------

#   Index:    0  1  2  3  4  5  6
#   String:   B  i  g  y  e  s  h
#   Neg Idx: -7 -6 -5 -4 -3 -2 -1

print("\n--- String Indexing ---")
print(f"First character: {name[0]}")      # B
print(f"Last character: {name[-1]}")      # h
print(f"Third character: {name[2]}")      # g
print(f"Second to last: {name[-2]}")      # s


# ---------------------------------------------------------------------
# 3. STRING SLICING
# ---------------------------------------------------------------------

# Syntax: str[start:end:step]
# start is included, end is NOT included

print("\n--- String Slicing ---")
text = "Python Programming"

print(f"First 6 chars: {text[:6]}")        # Python
print(f"From index 7: {text[7:]}")         # Programming
print(f"Chars 1 to 5: {text[1:6]}")        # ython
print(f"Reversed: {text[::-1]}")           # gnimmargorP nohtyP
print(f"Every 2nd char: {text[::2]}")      # Pto rgamn
print(f"Last 11 chars: {text[-11:]}")      # Programming


# ---------------------------------------------------------------------
# 4. STRING METHODS
# ---------------------------------------------------------------------

print("\n--- String Methods ---")
word = "Hello World"

# Case methods
print(f"upper(): {word.upper()}")          # HELLO WORLD
print(f"lower(): {word.lower()}")          # hello world
print(f"title(): {word.title()}")          # Hello World
print(f"capitalize(): {word.capitalize()}") # Hello world
print(f"swapcase(): {word.swapcase()}")    # hELLO wORLD

# Check methods
print(f"startswith('Hello'): {word.startswith('Hello')}")  # True
print(f"endswith('World'): {word.endswith('World')}")      # True
print(f"'World' in word: {'World' in word}")               # True

# Search methods
print(f"find('World'): {word.find('World')}")    # 6
print(f"find('xyz'): {word.find('xyz')}")        # -1 (not found)
print(f"count('l'): {word.count('l')}")          # 2

# Strip methods
padded = "  Hello  "
print(f"strip(): '{padded.strip()}'")      # 'Hello'
print(f"lstrip(): '{padded.lstrip()}'")    # 'Hello  '
print(f"rstrip(): '{padded.rstrip()}'")    # '  Hello'

# Replace method
print(f"replace('World', 'Python'): {word.replace('World', 'Python')}")

# Split and Join
sentence = "Python is awesome"
words = sentence.split()      # Splits into list
print(f"split(): {words}")    # ['Python', 'is', 'awesome']
joined = "-".join(words)
print(f"join(): {joined}")    # Python-is-awesome

# Other useful methods
print(f"isalpha(): {'Hello'.isalpha()}")      # True
print(f"isdigit(): {'123'.isdigit()}")        # True
print(f"isalnum(): {'Hello123'.isalnum()}")   # True
print(f"len(): {len(word)}")                  # 11


# ---------------------------------------------------------------------
# 5. STRING FORMATTING (f-strings)
# ---------------------------------------------------------------------

print("\n--- String Formatting ---")

name = "Krishna"
age = 16
score = 95.5

# f-string (recommended - Python 3.6+)
print(f"Hello {name}, you are {age} years old!")
print(f"Score: {score:.2f}")              # 2 decimal places
print(f"Score: {score:.0f}")              # No decimal places
print(f"Name in uppercase: {name.upper()}")

# Expression in f-string
print(f"10 years from now: {age + 10}")
print(f"5 * 3 = {5 * 3}")

# Format alignment
print(f"{'Left':<10}")    # Left aligned
print(f"{'Right':>10}")   # Right aligned
print(f"{'Center':^10}")  # Center aligned
print(f"{'Fill':*^10}")   # Fill with *

# Old style formatting (%)
print("Name: %s, Age: %d" % (name, age))

# .format() method
print("Name: {}, Age: {}".format(name, age))


# ---------------------------------------------------------------------
# 6. STRING OPERATIONS
# ---------------------------------------------------------------------

print("\n--- String Operations ---")

# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(f"Concatenation: {result}")

# Repetition
print(f"Repetition: {'Ha' * 3}")  # HaHaHa

# Membership test
print(f"'ell' in 'Hello': {'ell' in 'Hello'}")  # True


# ---------------------------------------------------------------------
# 7. PRACTICAL EXAMPLES
# ---------------------------------------------------------------------

print("\n--- Practical Examples ---")

# 1. Check if string is palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

test_string = "Racecar"
print(f"Is '{test_string}' a palindrome? {is_palindrome(test_string)}")

# 2. Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

test = "Python Programming"
print(f"Vowels in '{test}': {count_vowels(test)}")

# 3. Convert "Krishna" to "Kiha" using slicing
name = "Krishna"
converted = name[0] + name[2] + name[4] + name[5]
print(f"'{name}' to '{converted}'")

# 4. Greet user with f-string
user_name = input("\nEnter your name: ")
user_age = int(input("Enter your age: "))
print(f"Hello {user_name}, you are {user_age} years old! Welcome to Python!")
