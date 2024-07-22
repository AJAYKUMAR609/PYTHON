
#task-26
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import sys
import time

#
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from imdb import IMDbSearchPage

#
@pytest.fixture
def browser():

   chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"
   if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"chromedriver not found at path:{chromedriver_path}")

   os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

   # Create Chrome options
   chrome_options = Options()
   chrome_options.add_experimental_option("detach", True)

   driver = webdriver.Chrome(options=chrome_options)
   yield driver
   time.sleep(5)
   driver.quit()

def test_imdb_search(driver):
    # Navigate to IMDb search page
    driver.get("https://www.imdb.com/search/name/")

    # Create an instance of the IMDbSearchPage
    search_page = IMDbSearchPage(driver)

    # Enter search query (e.g., "Selenium")
    search_page.enter_search_query("kick")

    # Click the search button
    search_page.click_search_button()


    # Assert that the results page contains relevant information
    assert "kick" in driver.page_source

# Define the IMDbSearchPage class (similar to your previous code)
class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.XPATH, "//*[@id='suggestion-search']")
        self.search_button = (By.ID, "navbar-submit-button")
        self.advanced_search_link = (By.LINK_TEXT, "Advanced Search")

    def enter_search_query(self, query):
        self.driver.find_element(*self.search_box).send_keys(query)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    def navigate_to_advanced_search(self):
        self.driver.find_element(*self.advanced_search_link).click()


