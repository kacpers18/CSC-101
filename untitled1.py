# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GmoS5JpQ6erDMY3xQLXVVkjQ7D0sfx9z
"""

base = 10  # length of the base in cm
height = 4  # height of the triangle in cm

area = 0.5 * base * height
print("The area of the triangle is:", area, "square cm")

length = 50  # length of the garden in cm
width = 80   # width of the garden in cm
fenceLength = 15  # length of each fence section in cm

# Calculate the perimeter of the garden
gardenPerimeter = 2 * (length + width)

# Calculate the number of fences needed (rounding up)
import math
numberOfFences = math.ceil(gardenPerimeter / fenceLength)

print("You will need", numberOfFences, "fence sections to enclose the garden.")

# Total amount in cents
total_cents = 835

# Values of coins in cents
dollar_value = 100
quarter_value = 25
dime_value = 10

# Calculate the number of dollars
dollars = total_cents // dollar_value
remaining_cents = total_cents % dollar_value

# Calculate the number of quarters
quarters = remaining_cents // quarter_value
remaining_cents %= quarter_value

# Calculate the number of dimes
dimes = remaining_cents // dime_value

# Display the results
print("Dollars:", dollars)
print("Quarters:", quarters)
print("Dimes:", dimes)

print("One\nTwo\nThree")

# Ask for the user's name
name = input("Please enter your name: ")

# Print the message using escape characters
print(f'"{name}" is a common name.')

# Define the file path using escape characters
file_path = "C:\\Users\\Documents\\MyFile.txt"

# Print the file path
print(file_path)