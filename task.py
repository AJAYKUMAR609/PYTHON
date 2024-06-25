
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