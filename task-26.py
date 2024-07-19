
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

class ImdbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input_locator = (By.NAME, "q")  # Adjust the locator as needed

    def navigate_to_imdb_search_page(self):
        self.driver.get("https://www.imdb.com/search/name/")

    def fill_search_query(self, query):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_input_locator)
        )
        search_input.send_keys(query)

    # Add methods for other input fields, select boxes, and drop-down menus

if __name__ == "__main__":
    driver = webdriver.Chrome()
    imdb_search_page = ImdbSearchPage(driver)
    imdb_search_page.navigate_to_imdb_search_page()
    imdb_search_page.fill_search_query("Selenium")

    # Perform any additional actions (e.g., submit the form)

    # Remember to close the browser when done
    # driver.quit()
