#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 14:01:10 2025

@author: macbook
"""

#Task 1 write a program using a for a loop to print the square of numbers from 1 to 13
for i in range(1, 13):  # Loop through numbers from 1 to 13
    print(i ** 2)  # Print the square of the current number
    
    
    
    
    
# Task 2: Define a function to check grades
def check_grades(grades):
    # Iterate through each grade in the list
    for grade in grades:
        if grade >= 75:  # Check if the grade is 75 or more
            print("Pass")  # Print "Pass" if the condition is met
        else:
            print("No")  # Print "No" otherwise

# Test the function with a list of grades
check_grades([85, 70, 90, 60, 75])  # Example grades





# Task 3: Function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"  # Define the vowels
    count = {v: 0 for v in vowels}  # Initialize a dictionary to count each vowel
    total_vowels = 0  # Initialize total vowel count

    # Iterate through each character in the text
    for char in text:
        if char in vowels:  # Check if the character is a vowel
            count[char] += 1  # Increment the count for that vowel
            total_vowels += 1  # Increment the total vowel count

    print(f"Total vowels: {total_vowels}")  # Print total vowel count
    for v in vowels:
        print(f"{v}: {count[v]}")  # Print the count of each vowel

# Example string
count_vowels("Data is the language of the powerholders.")  # Example string





# Task 4: Data collection tool
def collect_numbers():
    numbers = []  # Initialize an empty list to store numbers

    while True:  # Start an infinite loop
        user_input = input("Enter a number (or 'done' to finish): ")  # Prompt user for input
        if user_input.lower() == 'done':  # Check if the user wants to finish
            break  # Exit the loop if 'done' is entered
        try:
            number = float(user_input)  # Try to convert input to float
            numbers.append(number)  # Add the number to the list
        except ValueError:
            print("Invalid input. Try again.")  # Handle non-numeric input

    # After exiting the loop, print results
    total_numbers = len(numbers)  # Count total numbers entered
    if total_numbers > 0:
        average = sum(numbers) / total_numbers  # Calculate average
        print(f"Total numbers entered: {total_numbers}")  # Print total count
        print(f"Average: {average:.2f}")  # Print average rounded to 2 decimal places
    else:
        print("No numbers were entered.")  # Handle case with no valid inputs

# Call the function to collect numbers
collect_numbers()  # Start the data collection tool



# Task 5: Analyze customer purchase data
purchases = [("Alice", 120), ("Bob", 80), ("Alice", 50), ("Bob", 20), ("Clara", 200)]  # Sample data

# Initialize a dictionary to store total purchases per customer
total_spent = {}

# Iterate over each purchase in the list
for customer, amount in purchases:
    if customer in total_spent:  # Check if the customer is already in the dictionary
        total_spent[customer] += amount  # Add to their total
    else:
        total_spent[customer] = amount  # Initialize their total

# Print out how much each customer spent in total
for customer, total in total_spent.items():
    print(f"{customer} spent ${total}")  # Print the total for each customer



# Task 6: Use wbdata to get population data

import wbdata
import datetime
import pandas as pd

def get_serbia_population():
    country = "RS"  # ISO code for Serbia
    indicator = {"SP.POP.TOTL": "Population"}  # World Bank indicator: total population

    # Date range from 2010 to 2020
    start_date = datetime.datetime(2010, 1, 1)
    end_date = datetime.datetime(2020, 12, 31)

    # Get the population data from World Bank
    data = wbdata.get_dataframe(indicator, country, (start_date, end_date))

    # Reset index to make 'date' a column
    data = data.reset_index()

    # Convert 'date' column from string to datetime
    data['date'] = pd.to_datetime(data['date'])

    # Print population per year
    for _, row in data.iterrows():
        year = row['date'].year
        population = int(row['Population']) if not pd.isnull(row['Population']) else 'N/A'
        print(f"Serbia - {year}: {population}")

# Run the function
get_serbia_population()



