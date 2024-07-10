
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


#
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

#


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


# Open the CoWIN website
driver.get("https://www.cowin.gov.in/")

# Click on the relevant link to open a new tab (you can adjust the XPath as needed)
driver.find_element_by_xpath('//a[contains(text(), "Register/Sign In")]').click()

# Print the title and current URL of the first tab (parent window)
print("Parent window title:", driver.title)

# Get the current window handle (parent window)
parent_window_handle = driver.current_window_handle

# Switch to the newly opened tab (second tab)
for window_handle in driver.window_handles:
    if window_handle != parent_window_handle:
        driver.switch_to.window(window_handle)
        break

# Print the title and current URL of the second tab (child window)
print("Child window title:", driver.title)

# Close the second tab
driver.close()

# Switch back to the first tab (parent window)
driver.switch_to.window(parent_window_handle)

# Clean up
driver.quit()




