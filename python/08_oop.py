# =====================================================================
# OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON
# Classes, Objects, Inheritance, 4 Pillars of OOP
# =====================================================================


# ---------------------------------------------------------------------
# 1. CLASSES AND OBJECTS
# ---------------------------------------------------------------------
# Class: Blueprint for creating objects
# Object: Instance of a class

print("--- Classes and Objects ---")

# Creating a class
class Car:
    """A class to represent a car."""
    
    # Class attribute (shared by all instances)
    wheels = 4
    
    def __init__(self, brand, color, speed):
        """Initialize car attributes."""
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.color = color
        self.speed = speed
    
    def start(self):
        """Start the car."""
        return f"{self.brand} car started!"
    
    def stop(self):
        """Stop the car."""
        return f"{self.brand} car stopped!"
    
    def accelerate(self, amount):
        """Increase speed."""
        self.speed += amount
        return f"{self.brand} speed is now {self.speed} km/h"
    
    def get_info(self):
        """Get car information."""
        return f"Brand: {self.brand}, Color: {self.color}, Speed: {self.speed}"

# Creating objects (instances)
car1 = Car("Toyota", "Red", 0)
car2 = Car("Honda", "Blue", 0)

print(car1.start())
print(car1.accelerate(60))
print(car1.get_info())
print()
print(car2.start())
print(car2.accelerate(80))
print(car2.get_info())

# Accessing class attribute
print(f"\nAll cars have {Car.wheels} wheels")


# ---------------------------------------------------------------------
# 2. INSTANCE ATTRIBUTE vs CLASS ATTRIBUTE
# ---------------------------------------------------------------------

print("\n--- Instance vs Class Attribute ---")

class Student:
    """Student class with class and instance attributes."""
    
    # Class attribute
    school = "Shivapuri Secondary School"
    
    def __init__(self, name, age, grade):
        # Instance attributes
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_info(self):
        return f"{self.name}, Age: {self.age}, Grade: {self.grade}, School: {self.school}"

# Instance attribute takes priority over class attribute
student1 = Student("Ram", 16, "A")
student2 = Student("Shyam", 17, "B")

print(student1.get_info())
print(student2.get_info())

# Override class attribute for specific instance
student1.school = "Different School"
print(f"\n{student1.name}'s school: {student1.school}")
print(f"{student2.name}'s school: {student2.school}")


# ---------------------------------------------------------------------
# 3. THE FOUR PILLARS OF OOP
# ---------------------------------------------------------------------

print("\n" + "=" * 60)
print("THE FOUR PILLARS OF OOP")
print("=" * 60)


# =====================================================================
# PILLAR 1: ENCAPSULATION
# =====================================================================
# Bundling data and methods together, restricting direct access

print("\n--- 1. ENCAPSULATION ---")

class BankAccount:
    """Bank account with encapsulation."""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        """Deposit money."""
        if amount > 0:
            self.__balance += amount
            return f"Deposited Rs.{amount}. Balance: Rs.{self.__balance}"
        return "Invalid deposit amount!"
    
    def withdraw(self, amount):
        """Withdraw money."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawn Rs.{amount}. Balance: Rs.{self.__balance}"
        return "Insufficient balance or invalid amount!"
    
    def get_balance(self):
        """Get current balance."""
        return f"Balance: Rs.{self.__balance}"

account = BankAccount("Ram", 1000)
print(account.deposit(500))
print(account.withdraw(300))
print(account.get_balance())
# print(account.__balance)  # Error: private attribute


# =====================================================================
# PILLAR 2: ABSTRACTION
# =====================================================================
# Hiding implementation details, showing only necessary features

print("\n--- 2. ABSTRACTION ---")

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract class for shapes."""
    
    @abstractmethod
    def area(self):
        """Calculate area (must be implemented by subclasses)."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter (must be implemented by subclasses)."""
        pass
    
    def display(self):
        """Concrete method (shared by all subclasses)."""
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

class Circle(Shape):
    """Circle class inheriting from Shape."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Cannot instantiate abstract class
# shape = Shape()  # Error!

circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle:")
circle.display()
print("\nRectangle:")
rectangle.display()


# =====================================================================
# PILLAR 3: INHERITANCE
# =====================================================================
# Derived class uses features of base class

print("\n--- 3. INHERITANCE ---")

# a. Single Inheritance
class Animal:
    """Base class - Animal."""
    
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        return f"{self.name} says {self.sound}!"
    
    def eat(self):
        return f"{self.name} is eating."

class Dog(Animal):
    """Derived class - Dog."""
    
    def __init__(self, name, breed):
        super().__init__(name, "Woof")  # Call parent constructor
        self.breed = breed
    
    def fetch(self):
        return f"{self.name} is fetching the ball!"
    
    def get_info(self):
        return f"Name: {self.name}, Breed: {self.breed}"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())    # From parent class
print(dog.eat())      # From parent class
print(dog.fetch())    # From child class
print(dog.get_info()) # From child class

print()

# b. Multiple Inheritance
class Flyable:
    """Mixin class for flying ability."""
    
    def fly(self):
        return f"{self.name} is flying!"

class Swimmable:
    """Mixin class for swimming ability."""
    
    def swim(self):
        return f"{self.name} is swimming!"

class Duck(Animal, Flyable, Swimmable):
    """Duck inherits from Animal, Flyable, and Swimmable."""
    
    def __init__(self, name):
        super().__init__(name, "Quack")

duck = Duck("Donald")
print(duck.speak())   # From Animal
print(duck.fly())     # From Flyable
print(duck.swim())    # From Swimmable

print()

# c. Multilevel Inheritance
class LivingThing:
    """Base class for all living things."""
    
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        return f"{self.name} is breathing."

class Animal(LivingThing):
    """Animal inherits from LivingThing."""
    
    def eat(self):
        return f"{self.name} is eating."

class Dog(Animal):
    """Dog inherits from Animal (which inherits from LivingThing)."""
    
    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Rex")
print(dog.breathe())  # From LivingThing
print(dog.eat())      # From Animal
print(dog.bark())     # From Dog


# =====================================================================
# PILLAR 4: POLYMORPHISM
# =====================================================================
# Same interface, different implementations

print("\n--- 4. POLYMORPHISM ---")

# a. Method Overriding
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Polymorphism in action
animals = [Dog(), Cat(), Duck()]
for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}")

print()

# b. Function with polymorphism
def animal_sound(animal):
    """Works with any animal that has a speak method."""
    return animal.speak()

print(animal_sound(Dog()))
print(animal_sound(Cat()))
print(animal_sound(Duck()))

print()

# c. Built-in polymorphism
print("Polymorphism with built-in functions:")
print(f"len('Hello'): {len('Hello')}")
print(f"len([1, 2, 3]): {len([1, 2, 3])}")
print(f"len({'a': 1, 'b': 2}): {len({'a': 1, 'b': 2})}")

print(f"\nint('5'): {int('5')}")
print(f"int(5.9): {int(5.9)}")


# ---------------------------------------------------------------------
# 4. PRACTICAL EXAMPLES
# ---------------------------------------------------------------------

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Student Management System
class Student:
    """Student class for managing student data."""
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = []
    
    def add_mark(self, mark):
        """Add a mark to the student."""
        self.marks.append(mark)
    
    def get_average(self):
        """Calculate average marks."""
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)
    
    def get_grade(self):
        """Get grade based on average."""
        avg = self.get_average()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"
    
    def get_info(self):
        """Get student information."""
        return f"Name: {self.name}, Age: {self.age}, Average: {self.get_average():.2f}, Grade: {self.get_grade()}"

print("\n--- Student Management System ---")
student1 = Student("Ram", 16, "A")
student1.add_mark(85)
student1.add_mark(90)
student1.add_mark(78)

student2 = Student("Shyam", 17, "B")
student2.add_mark(75)
student2.add_mark(80)
student2.add_mark(70)

print(student1.get_info())
print(student2.get_info())


# Example 2: Calculator using OOP
class Calculator:
    """Calculator class using OOP."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        return self.history

print("\n--- Calculator using OOP ---")
calc = Calculator()
print(f"10 + 5 = {calc.add(10, 5)}")
print(f"10 - 5 = {calc.subtract(10, 5)}")
print(f"10 * 5 = {calc.multiply(10, 5)}")
print(f"10 / 5 = {calc.divide(10, 5)}")
print(f"\nHistory: {calc.get_history()}")


# Example 3: Library System
class Book:
    """Book class."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    
    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"'{self.title}' has been borrowed."
        return f"'{self.title}' is not available."
    
    def return_book(self):
        self.is_available = True
        return f"'{self.title}' has been returned."

class Library:
    """Library class."""
    
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        return f"Added '{book.title}' to {self.name}."
    
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def get_available_books(self):
        return [book for book in self.books if book.is_available]

print("\n--- Library System ---")
library = Library("City Library")

book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Science", "Jane Doe")
book3 = Book("Machine Learning", "Bob Johnson")

print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))

print(f"\n{book1.borrow()}")
print(f"{book2.borrow()}")
print(f"\nAvailable books: {[b.title for b in library.get_available_books()]}")
print(f"{book1.return_book()}")
print(f"Available books: {[b.title for b in library.get_available_books()]}")


# Example 4: Employee Management
class Employee:
    """Base Employee class."""
    
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def get_info(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Salary: Rs.{self.salary}"
    
    def calculate_bonus(self):
        return self.salary * 0.1

class Manager(Employee):
    """Manager class inheriting from Employee."""
    
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department
    
    def calculate_bonus(self):
        return self.salary * 0.2  # Managers get 20% bonus
    
    def get_info(self):
        return f"{super().get_info()}, Department: {self.department}"

class Developer(Employee):
    """Developer class inheriting from Employee."""
    
    def __init__(self, name, employee_id, salary, language):
        super().__init__(name, employee_id, salary)
        self.language = language
    
    def calculate_bonus(self):
        return self.salary * 0.15  # Developers get 15% bonus
    
    def get_info(self):
        return f"{super().get_info()}, Language: {self.language}"

print("\n--- Employee Management ---")
employees = [
    Manager("Alice", "M001", 80000, "Engineering"),
    Developer("Bob", "D001", 60000, "Python"),
    Developer("Charlie", "D002", 65000, "JavaScript")
]

for emp in employees:
    print(f"{emp.get_info()}")
    print(f"  Bonus: Rs.{emp.calculate_bonus()}\n")
