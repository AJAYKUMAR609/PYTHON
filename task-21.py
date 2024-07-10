#task-21-using selenium python for checking wether cookie are generated during login
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
