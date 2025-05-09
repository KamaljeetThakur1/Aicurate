from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("login_url")
driver.find_element(By.ID, "username").send_keys("invalid_user")
driver.find_element(By.ID, "password").send_keys("wrong_pass")
driver.find_element(By.ID, "login_button").click()
assert "Authentication failed." in driver.page_source
driver.quit()