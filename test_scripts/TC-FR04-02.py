from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("login_url")
time.sleep(5)
driver.find_element(By.ID, "username").send_keys("valid_user")
driver.find_element(By.ID, "password").send_keys("valid_pass")
driver.find_element(By.ID, "login_button").click()
assert "Chat Input" in driver.page_source
driver.quit()