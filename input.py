from utils import add

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

name = input("Enter your name: ")
print(greet(name))
print(farewell(name))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"{x} + {y} = {add(x, y)}")
