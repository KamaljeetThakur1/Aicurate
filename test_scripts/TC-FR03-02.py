from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("login_url")
driver.find_element(By.ID, "username").send_keys("invalid_user")
driver.find_element(By.ID, "password").send_keys("wrong_pass")
driver.find_element(By.ID, "login_button").click()
time.sleep(2)
assert "Invalid username or password." in driver.page_source
driver.quit()