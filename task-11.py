#task-11 using selenium do adrop and dragable operation
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://jqueryui.com/droppable/")

# Switch to the iframe containing the draggable elements
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

# Locate the draggable element (white box)
draggable_element = driver.find_element(By.ID, "draggable")

# Locate the droppable element (yellow box)
droppable_element = driver.find_element(By.ID, "droppable")

# Perform the drag-and-drop action
actions = ActionChains(driver)
actions.drag_and_drop(draggable_element, droppable_element).perform()

# Verify that the drop was successful
drop_success_text = droppable_element.find_element(By.TAG_NAME, "p").text
if "Dropped!" in drop_success_text:
    print("Drop was successful")
else:
    print("Drop failed")

# Clean up
driver.quit()










