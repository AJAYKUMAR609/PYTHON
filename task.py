
# import module

from datetime import datetime

# get current date and time

current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

print("Current date & time : ", current_datetime)

# convert datetime obj to string

str_current_datetime = str(current_datetime)

# create a file object along with extension

file_name = str_current_datetime + ".txt"

file = open(file_name, 'w')

print("File created : ", file.name)

file.close()

# using time module

import time

# ts stores the time in seconds

ts = time.time()

# print the current timestamp

print(ts)
#

file_path = r"C:\Users\ajayk\OneDrive\Desktop\python1\kumar\function.txt"

with open(file_path, "a") as f:
    f.write("this is the method is done by using function")

#
file_path = r"C:\Users\ajayk\OneDrive\Desktop\python1\kumar\function.txt"

with open(file_path, "r") as f:
    file_contents = f.read()
    print(file_contents)


