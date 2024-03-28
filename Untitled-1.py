#program 1
list1=[10,501,22,37,100,999,87,351]
odd_num=[]
even_num=[]
for num in list1:
    if num % 2==1:
        odd_num.append(num)
    else:
        num % 2==0,
        even_num.append(num)
print("all even numbers:",even_num)
print("all odd numbers:",odd_num)

#program 2
list2=[10,501,22,37,100,999,87,351]
def prime_num(num):
    if num <=1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in list2 if prime_num(num)]
print("Prime numbers:", prime_numbers)


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

def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            print("File content:")
            print(file_content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")
# Example usage:
# Assuming you have a file named 'example.txt' with some content in the same directory as this script
# Call the function with the file name
read_text_file("example.txt")
