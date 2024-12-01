import math
from datetime import datetime, timedelta
"""
Exercise 1:
Create a Pizza class that could have ingredients added to it. Raise an error if an attempt is made to add a duplicate ingredient.
"""
class Pizza:
    def __init__(self):
        self.ingredients = set()
    
    def add_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            raise ValueError(f"{ingredient} is already on the pizza!")
        self.ingredients.add(ingredient)




"""
Exercise 2:
Create an Elevator class with methods to go up, go down, and get the current floor. The elevator should not be able to go below the ground floor (floor 0).
"""
class Elevator:
    def __init__(self):
        self.floor = 0

    def go_up(self):
        self.floor += 1
        return f"you are going up to {self.floor}"

    def go_down(self):
        if self.floor > 0:
            self.floor -= 1
        return self.floor

    def get_current_floor(self):
        return self.floor


"""
Exercise 3:
Create a class Stack with methods to push, pop, and check if the stack is empty. Raise an exception if a pop is attempted on an empty stack.
"""
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    def push(self, item):
        # Add the item to the top of the stack
        self.stack.append(item)

    def pop(self):
        # Raise an exception if the stack is empty
        if self.is_empty():
            raise IndexError("Pop attempted on an empty stack.")
        # Remove and return the top element of the stack
        return self.stack.pop()

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

"""
Exercise 4:
Design a BankAccount class with methods to deposit, withdraw, and check balance. Ensure that an account cannot go into a negative balance.
"""
class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def check_balance(self):
        return self.balance

"""
Exercise 5:
Create a class Person with attributes for name and age. Implement a method birthday that increases the person's age by one. Raise an exception if an age less than 0 is entered.
"""
class Person1:
    def __init__(self, name, age):
        if age <= 0:
            raise ValueError("Such person cannot exist")
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
        return self.age


"""
Exercise 6:
Create an Animal base class and a Dog and Cat derived classes. Each animal should have a sound method which returns the sound they make.
"""
class Animal:
    def sound(self):
        return None

class Dog(Animal):
    def sound(self):
        return 'Woof'

class Cat(Animal):
    def sound(self):
        return "Meow"


"""
Exercise 7:
Design a class Calculator with static methods for addition, subtraction, multiplication, and division. Division method should raise a ZeroDivisionError when trying to divide by zero.
"""
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y



"""
Exercise 8:
Create a class `Car` with attributes for speed and mileage. Raise a ValueError if a negative value for speed or mileage is entered.
"""
class Car:
    def __init__(self, speed, mileage):
        if speed < 0:
            raise ValueError("Speed cannot be negative")
        if mileage < 0:
            raise ValueError("Mileage cannot be negative")
        self.speed = speed
        self.mileage = mileage


"""
Exercise 9:
Create a Student class and a Course class. Each Course can enroll students and print a list of enrolled students.
"""
class Student1:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self):
        self.students = []  # Changed attribute name to `students`

    def enroll(self, student):
        if student not in self.students:
            self.students.append(student)
        else:
            raise ValueError(f"Student {student.name} is already enrolled.")

    def print_students(self):
        if not self.students:
            print("No students are enrolled in this course.")
        else:
            print("Enrolled students:")
            for student in self.students:
                print(f"- {student.name}")



"""
Exercise 10:
Create a Flight class with a destination, departure time, and a list of passengers. Implement methods to add passengers, change the destination, and delay the flight by a certain amount of time.
"""


class Flight:
    def __init__(self, destination, departure):
        self.destination = destination
        self.departure = departure
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination
        return self.destination

    def delay(self, delay_time):

        departure_time = datetime.strptime(self.departure, "%H:%M")

        new_departure_time = departure_time + timedelta(hours=delay_time)
 
        self.departure = new_departure_time.strftime("%H:%M")
        
        return self.departure


"""
Exercise 11:
Create a Library class with a list of Book objects. The Book class should have attributes for title and author. The Library class should have methods to add books and find a book by title.
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


"""
Exercise 12:
Design a class Matrix that represents a 2D matrix with methods for addition, subtraction, and multiplication. Implement error handling for operations that are not allowed (e.g., adding matrices of different sizes).
"""
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)  # Return a new Matrix object with the result

    def subtract(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)  # Return a new Matrix object with the result

    def multiply(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Number of columns in first matrix must equal number of rows in second matrix.")
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0]))) for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)  # Return a new Matrix object with the result

"""
Exercise 13:
Create a class Rectangle with attributes for height and width. Implement methods for calculating the area and perimeter of the rectangle. Also, implement a method is_square that returns true if the rectangle is a square and false otherwise.
"""
class Rectangle1:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def is_square(self):
        return self.height == self.width

"""
Exercise 14:
Design a class Circle with attributes for radius. Implement methods for calculating the area and the circumference of the circle. Handle exceptions for negative radius values.
"""
class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

"""
Exercise 15:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class Triangle2:
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("The sides do not form a valid triangle.")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


"""
Exercise 16:
Design a class Triangle with methods to calculate the area and perimeter. Implement error handling for cases where the given sides do not form a valid triangle.
"""
class AbstractShape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(AbstractShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.1416 * self.radius

class Rectangle(AbstractShape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

class Triangle(AbstractShape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

"""
Exercise 17:
Create a MusicPlayer class that contains a list of songs and methods to add songs, play a song, and skip to the next song. Also implement a method to shuffle the playlist.
"""
import random

class MusicPlayer:
    def __init__(self):
        self.songs = []
        self.current_song_index = 0

    def add_song(self, song):
        self.songs.append(song)

    def play_song(self):
        if self.songs:
            return f"Playing {self.songs[self.current_song_index]}"
        return "No songs in the playlist."
    def current_song(self):
        if self.songs:
            return self.songs[self.current_song_index]
        return None  
    def next_song(self):
        if self.songs:
            self.current_song_index = (self.current_song_index + 1) % len(self.songs)
            return self.play_song()
        return "No songs in the playlist."

    def shuffle(self):
        random.shuffle(self.songs)
        self.current_song_index = 0
    
    def playlist(self):
        return self.songs


"""
Exercise 18:
Design a Product class for an online store with attributes for name, price, and quantity. Implement methods to add stock, sell product, and check stock levels. Include error handling for attempting to sell more items than are in stock.
"""
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        self.quantity += quantity

    def sell(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")
        self.quantity -= quantity

    def check_stock(self):
        return self.quantity



"""
Exercise 19:
Create a VideoGame class with attributes for title, genre, and rating. Implement methods to change the rating, change the genre, and display game details.
"""
class VideoGame:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def change_rating(self, rating):
        self.rating = rating

    def change_genre(self, genre):
        self.genre = genre

    def display_details(self):
        return f"Title: {self.title}, Genre: {self.genre}, Rating: {self.rating}"



"""
Exercise 20:
Create a School class with a list of Teacher and Student objects. Teacher and Student classes should have attributes for name and age. The School class should have methods to add teachers, add students, and print a list of all people in the school.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    pass

class Student(Person):
    pass

class School:
    def __init__(self):
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def get_all(self):
        all_people = self.teachers + self.students
        return all_people  # Return the list of all people, not just print them

"""
Exercise 21:
Design a Card class to represent a playing card with suit and rank. Then design a Deck class that uses the Card class. The Deck class should have methods to shuffle the deck, deal a card, and check the number of remaining cards.
"""
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None

    def count(self):
        return len(self.cards)
