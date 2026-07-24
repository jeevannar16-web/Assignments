# =====================================================================
# DATA STRUCTURES IN PYTHON
# Lists, Tuples, Dictionaries, Sets
# =====================================================================


# =====================================================================
# PART 1: LISTS
# =====================================================================
# Lists are ordered, mutable, allow duplicates, heterogeneous

print("=" * 60)
print("LISTS IN PYTHON")
print("=" * 60)

# Creating lists
fruits = ["Apple", "Banana", "Orange", "Mango"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "Hello", 3.14, True, None]
empty_list = []

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Empty list: {empty_list}")


# ---------------------------------------------------------------------
# LIST INDEXING
# ---------------------------------------------------------------------

print("\n--- List Indexing ---")
#   Index:    0       1        2       3
#   List:  Apple   Banana  Orange   Mango

print(f"First element: {fruits[0]}")      # Apple
print(f"Last element: {fruits[-1]}")      # Mango
print(f"Second element: {fruits[1]}")     # Banana
print(f"Second to last: {fruits[-2]}")    # Orange


# ---------------------------------------------------------------------
# LIST SLICING
# ---------------------------------------------------------------------

print("\n--- List Slicing ---")
# Syntax: list[start:end:step]

print(f"First 2: {fruits[:2]}")          # ['Apple', 'Banana']
print(f"From index 1: {fruits[1:]}")     # ['Banana', 'Orange', 'Mango']
print(f"Middle: {fruits[1:3]}")          # ['Banana', 'Orange']
print(f"Reversed: {fruits[::-1]}")       # ['Mango', 'Orange', 'Banana', 'Apple']


# ---------------------------------------------------------------------
# LIST MUTABILITY
# ---------------------------------------------------------------------

print("\n--- List Mutability ---")
fruits[0] = "Grapes"
print(f"After changing first element: {fruits}")  # ['Grapes', 'Banana', 'Orange', 'Mango']


# ---------------------------------------------------------------------
# LIST METHODS
# ---------------------------------------------------------------------

print("\n--- List Methods ---")
numbers = [39, 22, 89, 11, 60]
print(f"Original: {numbers}")

# sort() - Sorts the list in ascending order
numbers.sort()
print(f"After sort(): {numbers}")          # [11, 22, 39, 60, 89]

# sort(reverse=True) - Sorts in descending order
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")  # [89, 60, 39, 22, 11]

# reverse() - Reverses the list
numbers.reverse()
print(f"After reverse(): {numbers}")       # [11, 22, 39, 60, 89]

# append() - Adds element at the end
numbers.append(100)
print(f"After append(100): {numbers}")

# insert() - Adds element at specific index
numbers.insert(2, 50)
print(f"After insert(2, 50): {numbers}")

# pop() - Removes and returns element at index
popped = numbers.pop()
print(f"After pop(): {numbers}, popped: {popped}")

popped = numbers.pop(1)
print(f"After pop(1): {numbers}, popped: {popped}")

# remove() - Removes first occurrence of element
numbers.remove(50)
print(f"After remove(50): {numbers}")

# clear() - Removes all elements
temp_list = [1, 2, 3]
temp_list.clear()
print(f"After clear(): {temp_list}")

# index() - Returns index of first occurrence
print(f"Index of 39 in {numbers}: {numbers.index(39)}")

# count() - Returns count of occurrences
print(f"Count of 22 in {numbers}: {numbers.count(22)}")

# copy() - Returns a copy of the list
copied = numbers.copy()
print(f"Copied list: {copied}")

# extend() - Adds elements from another list
numbers.extend([200, 300])
print(f"After extend([200, 300]): {numbers}")


# ---------------------------------------------------------------------
# LOOPING THROUGH A LIST
# ---------------------------------------------------------------------

print("\n--- Looping Through a List ---")
fruits = ["Apple", "Banana", "Mango", "Orange"]

# Simple for loop
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# Using enumerate (index + value)
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Using range and len
print("\nUsing range:")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")


# ---------------------------------------------------------------------
# MATHEMATICAL FUNCTIONS WITH LISTS
# ---------------------------------------------------------------------

print("\n--- Mathematical Functions ---")
numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}")
print(f"max(): {max(numbers)}")      # 50
print(f"min(): {min(numbers)}")      # 10
print(f"sum(): {sum(numbers)}")      # 150
print(f"len(): {len(numbers)}")      # 5
print(f"avg: {sum(numbers)/len(numbers)}")  # 30.0


# =====================================================================
# PART 2: TUPLES
# =====================================================================
# Tuples are ordered, IMMUTABLE, allow duplicates, heterogeneous

print("\n" + "=" * 60)
print("TUPLES IN PYTHON")
print("=" * 60)

# Creating tuples
colors = ("Red", "Green", "Blue")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "Hello", 3.14, True)
single = (1,)        # Single element tuple (comma is required)
empty_tuple = ()

print(f"Colors: {colors}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Single element: {single}")
print(f"Empty tuple: {empty_tuple}")


# ---------------------------------------------------------------------
# TUPLE INDEXING
# ---------------------------------------------------------------------

print("\n--- Tuple Indexing ---")
print(f"First element: {colors[0]}")      # Red
print(f"Last element: {colors[-1]}")      # Blue


# ---------------------------------------------------------------------
# TUPLE SLICING
# ---------------------------------------------------------------------

print("\n--- Tuple Slicing ---")
print(f"First 2: {colors[:2]}")          # ('Red', 'Green')
print(f"From index 1: {colors[1:]}")     # ('Green', 'Blue')


# ---------------------------------------------------------------------
# TUPLE IMMUTABILITY
# ---------------------------------------------------------------------

print("\n--- Tuple Immutability ---")
# This would cause an error:
# colors[0] = "Yellow"  # TypeError: 'tuple' object does not support item assignment
print("Tuples are immutable - cannot change values after creation!")


# ---------------------------------------------------------------------
# TUPLE METHODS
# ---------------------------------------------------------------------

print("\n--- Tuple Methods ---")
tup = (1, 3, 4, 2, 2, 5, 7)
print(f"Tuple: {tup}")
print(f"count(2): {tup.count(2)}")    # 2 (how many times 2 appears)
print(f"index(5): {tup.index(5)}")    # 5 (index of value 5)
print(f"len(): {len(tup)}")           # 7


# ---------------------------------------------------------------------
# LOOPING THROUGH TUPLE
# ---------------------------------------------------------------------

print("\n--- Looping Through Tuple ---")
fruits = ("Apple", "Mango", "Banana")
for fruit in fruits:
    print(f"  - {fruit}")


# ---------------------------------------------------------------------
# TUPLE PACKING AND UNPACKING
# ---------------------------------------------------------------------

print("\n--- Tuple Packing and Unpacking ---")
# Packing
person = "Ram", 20, "Kathmandu"
print(f"Packed: {person}")

# Unpacking
name, age, city = person
print(f"Name: {name}, Age: {age}, City: {city}")


# =====================================================================
# PART 3: DICTIONARIES
# =====================================================================
# Dictionaries are key-value pairs, mutable, indexed, no duplicate keys

print("\n" + "=" * 60)
print("DICTIONARIES IN PYTHON")
print("=" * 60)

# Creating dictionaries
student = {
    "Name": "Bigyesh",
    "Age": 26,
    "Occupation": "Instructor",
    "Skills": ["Python", "ML", "AI"]
}

print(f"Student: {student}")


# ---------------------------------------------------------------------
# ACCESSING DICTIONARY ELEMENTS
# ---------------------------------------------------------------------

print("\n--- Accessing Elements ---")
print(f"Name: {student['Name']}")           # Using brackets
print(f"Age: {student.get('Age')}")         # Using get()
print(f"City: {student.get('City', 'N/A')}")  # Default value if key not found


# ---------------------------------------------------------------------
# DICTIONARY METHODS
# ---------------------------------------------------------------------

print("\n--- Dictionary Methods ---")

# keys() - Returns list of keys
print(f"keys(): {student.keys()}")

# values() - Returns list of values
print(f"values(): {student.values()}")

# items() - Returns list of key-value pairs
print(f"items(): {student.items()}")

# update() - Updates dictionary
student.update({"Age": 27, "City": "Kathmandu"})
print(f"After update: {student}")

# pop() - Removes and returns value
removed = student.pop("Occupation")
print(f"After pop('Occupation'): {student}")
print(f"Removed: {removed}")

# popitem() - Removes last item
last_item = student.popitem()
print(f"After popitem(): {student}")
print(f"Last item: {last_item}")

# clear() - Removes all items
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print(f"After clear(): {temp_dict}")

# copy() - Returns a copy
copied = student.copy()
print(f"Copied: {copied}")

# setdefault() - Gets value or sets default
student.setdefault("Phone", "N/A")
print(f"After setdefault: {student}")

# fromkeys() - Creates dict with same values
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(f"fromkeys(): {new_dict}")


# ---------------------------------------------------------------------
# LOOPING THROUGH DICTIONARY
# ---------------------------------------------------------------------

print("\n--- Looping Through Dictionary ---")
student = {"name": "Ram", "age": 20, "city": "Kathmandu"}

# Looping through keys
print("Keys:")
for key in student:
    print(f"  {key}")

# Looping through values
print("\nValues:")
for value in student.values():
    print(f"  {value}")

# Looping through key-value pairs
print("\nKey-Value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")


# ---------------------------------------------------------------------
# NESTED DICTIONARY
# ---------------------------------------------------------------------

print("\n--- Nested Dictionary ---")
students = {
    "student1": {
        "name": "Ram",
        "age": 20,
        "marks": [85, 90, 78]
    },
    "student2": {
        "name": "Shyam",
        "age": 22,
        "marks": [75, 80, 70]
    },
    "student3": {
        "name": "Hari",
        "age": 19,
        "marks": [60, 65, 55]
    }
}

# Accessing nested values
print(f"Student1 Name: {students['student1']['name']}")
print(f"Student2 Age: {students['student2']['age']}")

# Looping through nested dictionary
print("\nAll Students:")
for student_id, info in students.items():
    print(f"\n{student_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")


# =====================================================================
# PART 4: SETS
# =====================================================================
# Sets are unindexed, mutable, NO duplicates

print("\n" + "=" * 60)
print("SETS IN PYTHON")
print("=" * 60)

# Creating sets
numbers = {10, 20, 10, 30, 40, 40}
fruits = {"Apple", "Banana", "Orange"}
empty_set = set()  # {} creates empty dict, not set

print(f"Numbers (duplicates removed): {numbers}")  # {10, 20, 30, 40}
print(f"Fruits: {fruits}")
print(f"Empty set: {empty_set}")


# ---------------------------------------------------------------------
# SET METHODS
# ---------------------------------------------------------------------

print("\n--- Set Methods ---")

# add() - Adds element
numbers.add(50)
print(f"After add(50): {numbers}")

# remove() - Removes element (raises error if not found)
numbers.remove(20)
print(f"After remove(20): {numbers}")

# discard() - Removes element (no error if not found)
numbers.discard(100)  # No error
print(f"After discard(100): {numbers}")

# pop() - Removes and returns arbitrary element
popped = numbers.pop()
print(f"After pop(): {numbers}, popped: {popped}")

# clear() - Removes all elements
temp_set = {1, 2, 3}
temp_set.clear()
print(f"After clear(): {temp_set}")

# copy() - Returns a copy
copied = numbers.copy()
print(f"Copied: {copied}")


# ---------------------------------------------------------------------
# SET OPERATIONS
# ---------------------------------------------------------------------

print("\n--- Set Operations ---")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union (|) - All elements from both sets
print(f"Union (|): {set1 | set2}")

# Intersection (&) - Common elements
print(f"Intersection (&): {set1 & set2}")

# Difference (-) - Elements in set1 but not in set2
print(f"Difference set1-set2: {set1 - set2}")
print(f"Difference set2-set1: {set2 - set1}")

# Symmetric Difference (^) - Elements in either set but not both
print(f"Symmetric Difference (^): {set1 ^ set2}")

# Subset and Superset
set3 = {1, 2}
print(f"\nSet 3: {set3}")
print(f"set3 is subset of set1: {set3.issubset(set1)}")
print(f"set1 is superset of set3: {set1.issuperset(set3)}")

# isdisjoint() - True if no common elements
set4 = {10, 20}
print(f"set1 and set4 disjoint: {set1.isdisjoint(set4)}")


# =====================================================================
# PART 5: PRACTICAL EXAMPLES
# =====================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# 1. Find duplicate elements in a list
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

numbers = [1, 2, 3, 2, 4, 3, 5]
print(f"Duplicates in {numbers}: {find_duplicates(numbers)}")

# 2. Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"Merged dictionaries: {merged}")

# 3. Find common elements in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"Common elements: {common}")

# 4. Count frequency of elements
def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(f"Frequency: {count_frequency(words)}")
