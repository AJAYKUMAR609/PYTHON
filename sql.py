#
# test_imdb_search.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Set up Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless for testing
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
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

    # Wait for search results (you can add explicit waits here)

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

