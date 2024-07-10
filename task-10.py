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
