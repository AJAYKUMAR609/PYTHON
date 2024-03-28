
#program to add first and last numbers

num = 1579
#convert num into string
num = str(num)
#str into integer
first_digit = int(num[0])

last_digit = int(num[-1])

addition = first_digit + last_digit

print("Addition of first and last digit of the number is:", addition)

#program to import time and create a text file
import os
from datetime import datetime


def create_timestamp_file():
    # Get the current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a text file with the current timestamp as its name
    filename = f"{current_time}.txt"

    # Write the current timestamp into the file
    with open(filename, 'w') as file:
        file.write(current_time)

    print(f"File '{filename}' created with the content of the current timestamp.")

# Call the function to create the timestamp file
create_timestamp_file()

# Define the number of rows for the pyramid
num_rows = 20

# Outer loop for rows
for i in range(1, num_rows + 1):
    # Print spaces for left alignment
    print(" " * (num_rows - i), end="")

    # Inner loop for printing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Move to the next line
    print()


def count_vowels(string):
    # Initialize counters for each vowel
    count_a = count_e = count_i = count_o = count_u = 0

    # Convert the string to lowercase to handle both upper and lower case vowels
    string = string.lower()

    # Iterate through each character in the string
    for char in string:
        if char == 'a':
            count_a += 1
        elif char == 'e':
            count_e += 1
        elif char == 'i':
            count_i += 1
        elif char == 'o':
            count_o += 1
        elif char == 'u':
            count_u += 1

    # Calculate the total number of vowels
    total_vowels = count_a + count_e + count_i + count_o + count_u

    # Print the counts of each individual vowel and total number of vowels
    print("Count of 'A':", count_a)
    print("Count of 'E':", count_e)
    print("Count of 'I':", count_i)
    print("Count of 'O':", count_o)
    print("Count of 'U':", count_u)
    print("Total number of vowels:", total_vowels)


# Test the function with the given string
input_string = "guvi geeks network private limited"
count_vowels(input_string)


def remove_vowels(input_string):
    # string containing all vowels of uppercase and lowercase
    vowels = "aeiouAEIOU"

    # Use list comprehension to create a new string with vowels removed
    new_string = ''.join(char for char in input_string if char not in vowels)

    return new_string


# Test the function
input_string = "Hello, World! This is a test string."
result = remove_vowels(input_string)
print("Original string:", input_string)
print("String with vowels removed:", result)