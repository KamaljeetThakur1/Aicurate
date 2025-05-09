from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("login_url")
driver.find_element(By.ID, "login_button").click()
assert "Credentials cannot be empty." in driver.page_source
driver.quit()