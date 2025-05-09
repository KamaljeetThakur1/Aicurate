from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("login_url")
driver.find_element(By.ID, "username").send_keys("invalid_format@")
driver.find_element(By.ID, "password").send_keys("valid_pass")
driver.find_element(By.ID, "login_button").click()
assert "Invalid username format." in driver.page_source
driver.quit()