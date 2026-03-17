name = input("Enter your name: ")
text = input("Enter a word: ")

print("\n------ Result ------")
print(f"Hello {name}!")
print(f"Your word in uppercase is: {text.upper()}")
print("--------------------")

print("*** Script Completed Successfully ***")

def greet(name):
    return f"Hello, {name}!"

# This script accepts user input and performs string operations
# Author: KWNS-q

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer!")
