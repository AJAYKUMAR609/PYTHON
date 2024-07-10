import audioop

import self

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


class add:
    def __init__(a,b,c):
     a.b=b
     a.c=c
     a.d=a.b+a.c
d=add(4,5)
print(d.b+d.c)

class sub:
    def __init__(v,x,y):
       v.x=x
       v.y=y
       v.z=v.x-v.y
z=sub(3,8)
print(z.x-z.y)

#creat a python class called circle with constructor.
class Circle:
    # constructor
    def __init__(self):
        # initializing instance variable
        self.num = [10, 501, 22, 37, 100, 999, 87, 351]

    # a method
    def read_number(self):
        print(self.num)

# creating object of the class. This invokes constructor
obj = Circle()

# calling the instance method using the object obj
obj.read_number()

#creating proper member variables inside the task
class MyClass:
    # Private class variable
    __pi = 3.141

    # Public instance variable
    a = 33

    # Private method
    def __privMeth(self):
        print("I'm inside class MyClass")

    # Public method
    def hello(self):
        print("Private Variable value: ", MyClass.a)

# Creating an object of the class
foo = MyClass()

# Calling the public method
foo.hello()

# Accessing the public class variable
print(foo.a)

# Accessing the private class variable (this will raise an AttributeError)
# print(foo.__pi)

#creating two class methods area and perimeter which are going to calculate area and perimeter

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        # Area of a circle is πr²
        return self.radius**2 * 3.141

    def perimeter(self):
        # Perimeter (Circumference) of a circle is 2πr
        return 2 * self.radius * 3.141

# Creating a new Circle object with radius 7
NewCircle = Circle(7)
print(NewCircle.area())
print(NewCircle.perimeter())

#task-9 displaying webpage name and current url
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.by import By
# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.saucedemo.com/inventory.html")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
page_source=driver.page_source
filename='webpage_task_11.txt'
with open(filename,'w',
          encoding='utf-8')as f:
    f.write(page_source)
print(f"webpage content saved to '{filename}'.")
print(driver.title)
print(driver.current_url)

#task-10
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from selenium.webdriver.common.by import By
# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.cowin.gov.in/")
driver.find_element(By.XPATH,'//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a').click()
print(driver.title)
print(driver.current_url)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.find_element(By.XPATH,'//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a').click()
print(driver.title)
print(driver.current_url)
driver.switch_to.window(driver.window_handles[-1])
driver.close()

#
#task20-using selenium download photos and monthly reports

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from selenium.webdriver.common.by import By
# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.cowin.gov.in/")
driver.find_element(By.XPATH,'//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a').click()
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH,'//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a').click()
print(driver.title)
print(driver.current_url)
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[1])
driver.close()

#task-labour.gov.in

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://labour.gov.in/")
time.sleep(5)

# Find the link to the monthly progress report
documents_menu = driver.find_element(By.LINK_TEXT, "Documents")
actions = ActionChains(driver)
actions.move_to_element(documents_menu).perform()
time.sleep(3)
monthly_report_link = driver.find_element(By.LINK_TEXT, "Monthly Progress Report")
monthly_report_url = monthly_report_link.get_attribute("href")

# Make a request to download the report
report_response = requests.get(monthly_report_url)
with open(r"C:\Users\ajayk\OneDrive\Desktop\python1\Monthly_Progress_Report.pdf", "wb") as file:
    file.write(report_response.content)

print("Monthly progress report downloaded successfully")


#task-labour.gov.in for photos

import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajayk\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://labour.gov.in/")
time.sleep(5)

# Go to media menu and photo gallery
driver.find_element(By.LINK_TEXT, "Media").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Click for more info of Press Releases").click()
driver.find_element(By.LINK_TEXT, "Photo Gallery").click()
time.sleep(5)

# Create the photo folder if it doesn't exist
photo_folder = r"C:\Users\ajayk\OneDrive\Desktop\python1\Photo Gallery"
if not os.path.exists(photo_folder):
    os.makedirs(photo_folder)

# Get all image elements
photos = driver.find_elements(By.CSS_SELECTOR, "img")[:10]

# Download and save images
for index, photo in enumerate(photos):
    photo_url = photo.get_attribute("src")
    photo_response = requests.get(photo_url)
    with open(os.path.join(photo_folder, f"photo_{index + 1}.jpg"), "wb") as file:
        file.write(photo_response.content)
        print(f"Downloaded photo {index + 1}")

print("Photo download is complete!")


#task-21-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.by import By
# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.saucedemo.com/inventory.html")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

# Step 4: Get cookies after login
time.sleep(2)  # Wait for the page to load
cookies_after_login = driver.get_cookies()
print("\nCookies after login:")
for cookie in cookies_after_login:
    print(f"{cookie['name']}: {cookie['value']}")

# Step 5: Verify cookies (you can add custom verification logic here)

# Step 6: Log out (if applicable)
# Example: driver.find_element_by_id("logout-button").click()

# Clean up
driver.quit()

#task-10-print no of followers are there in guvi-insta page
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.instagram.com/guviofficial/")
time.sleep(10)  # Add a delay to allow page content to load

# Use WebDriverWait to wait for elements to be present
wait = WebDriverWait(driver, 10)
followers_element = wait.until(EC.presence_of_element_located((By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button")))
following_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button")))

# Extract the follower and following counts
followers_count = followers_element.get_attribute("title")
following_count = following_element.text

print(f"Followers: {followers_count}")
print(f"Following:{following_count}")

# Quit the WebDriver
driver.quit()







#task-11 using selenium do adrop and dragable operation
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://jqueryui.com/droppable/")

# Switch to the iframe containing the draggable elements
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

# Locate the draggable element (white box)
draggable_element = driver.find_element(By.ID, "draggable")

# Locate the droppable element (yellow box)
droppable_element = driver.find_element(By.ID, "droppable")

# Perform the drag-and-drop action
actions = ActionChains(driver)
actions.drag_and_drop(draggable_element, droppable_element).perform()

# Verify that the drop was successful
drop_success_text = droppable_element.find_element(By.TAG_NAME, "p").text
if "Dropped!" in drop_success_text:
    print("Drop was successful")
else:
    print("Drop failed")

# Clean up
driver.quit()


























