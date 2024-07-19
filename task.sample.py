
###task-01 add employee details in orange hrm portal
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)


# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Set an explicit wait of 10 seconds
wait = WebDriverWait(driver, 10)

#ak

# Log in with valid credentials (you can modify this part)
username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
username_input.send_keys("Admin")  # Replace with the actual username

password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password_input.send_keys("admin123")  # Replace with the actual password

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
login_button.click()

# Navigate to the PIM module
pim_module_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span")))
pim_module_link.click()

# Click on 'Add Employee'
add_employee_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")))
add_employee_button.click()

# Fill in employee details
first_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
first_name_input.send_keys("vijay")  # Replace with the actual first name

middle_name_input = driver.find_element(By.NAME, "middleName")
middle_name_input.send_keys("ram")  # Replace with the actual middle name

last_name_input = driver.find_element(By.NAME, "lastName")
last_name_input.send_keys("KUMAR")  # Replace with the actual last name
#

# Save the employee details
save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")))
save_button.click()

# Add license number
drivers_License_Number_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')))
drivers_License_Number_input.send_keys("7396")

# Add license expiry date

license_expiry_date_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input')))
license_expiry_date_input.send_keys("2034-12-31")

# Add nationality
nationality_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]')))
nationality_dropdown.click()
nationality_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Indian']")))
nationality_option.click()

# Add marital status
marital_status_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]')))
marital_status_dropdown.click()
marital_status_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Single']")))
marital_status_option.click()

# Add date of birth
date_of_birth_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input')))
date_of_birth_input.send_keys("1996-01-13")

# Select gender
gender_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label')))
gender_radio_button.click()

# Save the employee details
save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')))
save_button.click()
#
blood_type=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]')))
blood_type.click()
blood_type = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='B+']")))
blood_type.click()
#
# Save the employee details
save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button')))
save_button.click()

driver.close()
##task-02 update employee details
#import os
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)


# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Set an explicit wait of 10 seconds
wait = WebDriverWait(driver, 30)  # Increase the timeout to 30 seconds


#ak

# Log in with valid credentials (you can modify this part)
username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
username_input.send_keys("Admin")  # Replace with the actual username

password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password_input.send_keys("admin123")  # Replace with the actual password

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
login_button.click()

# Navigate to the PIM module
pim_module_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span")))
pim_module_link.click()


# Step 3: Select an employee from the list
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Employee List"))).click()

Employee_name_input=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')))
Employee_name_input.send_keys("Keerthi")

#click on search
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')))
search_button.click()


#//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]

action_button=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]')))
action_button.click()
# Edit employee details

# Add license expiry date
license_expiry_date_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input')))
license_expiry_date_input.send_keys("2032-04-02")


# Save the employee details
save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')))
save_button.click()