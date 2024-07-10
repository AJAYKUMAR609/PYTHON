#task-25 using python selenium do explicit wait and expected out put
import os
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

# Open the IMDb advanced name search page
driver.get("https://www.imdb.com/search/name/")

# Set an explicit wait of 10 seconds
wait = WebDriverWait(driver, 10)

# Wait for the search input element to be visible
search_input = wait.until(EC.visibility_of_element_located((By.NAME, "q")))

# Enter the search query (e.g., "Selenium")
search_input.send_keys("Selenium")

# Perform any additional actions (e.g., submit the form)

# Remember to close the browser when done
# driver.quit()
