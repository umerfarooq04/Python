# main.py
from utils import add, subtract, multiply, divide



def greet(name):
    return f"Hello, {name}!"

print(greet("Umer"))

def farewell(name):
    return f"Goodbye, {name}!"

print(greet("Umer"))
print(farewell("Umer"))

# utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b



x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"Add: {add(x, y)}")
print(f"Subtract: {subtract(x, y)}")
print(f"Multiply: {multiply(x, y)}")
print(f"Divide: {divide(x, y)}")