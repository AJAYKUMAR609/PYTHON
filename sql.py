import os
import time
import pytest
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
# Set up WebDriver and navigate to IMDb homepage
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.imdb.com/")

# Now try interacting with elements on this page
# ...


# Define Page Object Model (POM) elements
class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "navbar-query")
        self.search_button = (By.ID, "navbar-submit-button")
        self.advanced_search_link = (By.LINK_TEXT, "Advanced Search")


    def enter_search_query(self, query):
        self.driver.find_element(*self.search_box).send_keys(query)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    def navigate_to_advanced_search(self):
        self.driver.find_element(*self.advanced_search_link).click()

# Create an instance of the IMDbSearchPage
search_page = IMDbSearchPage(driver)


# Enter search query (e.g., "Tom Hanks")
search_page.enter_search_query("Tom Hanks")

# Click the search button
search_page.click_search_button()

# Wait for search results to load (explicit wait)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "findResult")))

# Perform additional actions if needed (e.g., select boxes, drop-down menus)

# Close the browser
driver.quit()


