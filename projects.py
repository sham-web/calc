# 1.Calculator:

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

# Main calculator function
# def calculator():
#     print("Select an operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
    
#     choice = input("Enter your choice (1/2/3/4): ")
    
#     if choice in ['1', '2', '3', '4']:
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
        
#         if choice == '1':
#             print(f"The result is: {add(num1, num2)}")
#         elif choice == '2':
#             print(f"The result is: {subtract(num1, num2)}")
#         elif choice == '3':
#             print(f"The result is: {multiply(num1, num2)}")
#         elif choice == '4':
#             print(f"The result is: {divide(num1, num2)}")
#     else:
#         print("Invalid choice. Please try again.")

# Run the calculator
# calculator()

# ______________________________________________________________________________
# 2. project 
# import random

# def generate_story():
#     # Predefined story templates
#     templates = [
#         "Once upon a time, there was a {adjective} {animal} named {name}. It loved to {verb} every day in the {place}.",
#         "In a {adjective} forest, a {animal} named {name} discovered a magical {object}. It changed their life forever!",
#         "{name}, the {adjective} {animal}, decided to {verb} to the {place} in search of a {object}. What an adventure!"
#     ]


#     # Random words for the placeholders
#     adjectives = ["brave", "lazy", "curious", "friendly", "mysterious"]
#     animals = ["cat", "dog", "fox", "rabbit", "unicorn"]
#     names = ["Charlie", "Luna", "Max", "Bella", "Oscar"]
#     verbs = ["explore", "jump", "play", "run", "swim"]
#     places = ["jungle", "beach", "mountain", "castle", "garden"]
#     objects = ["treasure", "key", "map", "book", "potion"]

#     # Randomly select a story template
#     template = random.choice(templates)

#     # Replace placeholders with random words
#     story = template.format(
#         adjective=random.choice(adjectives), #adjective=lazy
#         animal=random.choice(animals),  #animal="cat"
#         name=random.choice(names),
#         verb=random.choice(verbs),
#         place=random.choice(places),
#         object=random.choice(objects)
#     )

#     print(story)

# # Generate and display a story
# print("Here’s your story:")
# generate_story()

# ________________________________________________________________________________
# 3.# projects:
# # Function to generate an acronym
# def generate_acronym(phrase):
#     words = phrase.split()  # Split the phrase into words
#     # acronym = ''.join([word[0].upper() for word in words])  # Take the first letter of each word and capitalize it
#     acronym = ""
#     for word in words:
#         acronym =acronym+ word[0].upper()

#     return acronym

# # Input a phrase
# phrase = input("Enter a phrase: ")
# print("Acronym:", generate_acronym(phrase))

# # central processing unit:
# phrase = input("Enter a phrase: ")

# words=phrase.split()
# print(words)
# acronym=""
# for word in words:
#     acronym=acronym+word[0].upper()
# print(acronym)
# -----------------------------------------------------------------
# 4.project:
# Set the correct password
# correct_password = "python123"

# while True:
#     # Prompt the user to enter the password
#     user_password = input("Enter the password: ")

#     # Check if the entered password is correct
#     if user_password == correct_password:
#         print("Access Granted!")
#         break  # Exit the loop when the correct password is entered
#     else:
#         print("Incorrect password. Please try again.")
# ----------------------------------------------------------------------------
# 5.project:
# # Python program to convert Fahrenheit to Celsius

# # Function to convert Fahrenheit to Celsius
# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# # Input: Fahrenheit temperature
# fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# # Convert to Celsius
# celsius = fahrenheit_to_celsius(fahrenheit)

# # Output: Celsius temperature
# print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")

# --------------------------------------------------------------------------
# 6.project:
# # Program to take multiple inputs using a while loop

# inputs = []  # List to store inputs

# print("Enter numbers one by one. Type 'done' to stop.")

# while True:
#     user_input = input("Enter a number: ")
#     if user_input.lower() == 'done':  # Check if the user wants to stop
#         break
#     try:
#         number = float(user_input)  # Convert input to a number
#         inputs.append(number)  # Add to the list
#     except ValueError:
#         print("Invalid input. Please enter a number.")

# print("You entered:", inputs)

# op:
# Enter numbers one by one. Type 'done' to stop.
# Enter a number: 12
# Enter a number: 45.6
# Enter a number: done
# You entered: [12.0, 45.6]

# -----------------------------------------------------------
7.# Convert emoji into text in Python
import emoji

# Input string containing emojis
text_with_emojis = "I love Python 🐍  and programming 💻! 😀"

# Convert emojis to text
text_to_words = emoji.demojize(text_with_emojis)

print("Converted text:", text_to_words)

import emoji

# # Text containing emoji shortcodes
# text_with_shortcodes = "I love Python programming :snake: and coffee :coffee:!"

# # Convert shortcodes to emojis
# text_with_emojis = emoji.emojize(text_with_shortcodes, language='alias')

# print("Text with emojis:", text_with_emojis)
# # op:
# # Text with emojis: I love Python programming 🐍 and coffee ☕!


# git hub:website
# git :software