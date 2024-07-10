
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
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
print(driver.current_url)
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,'//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a').click()
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
print(driver.current_url)
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.quit()

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

