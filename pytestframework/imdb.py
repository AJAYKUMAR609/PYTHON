from selenium.webdriver.common.by import By


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