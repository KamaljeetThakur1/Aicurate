
# Sample automation script for business user attributes
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/login')
driver.find_element(By.ID, 'username').send_keys('businessUser')
driver.find_element(By.ID, 'password').send_keys('Password123')
driver.find_element(By.ID, 'loginButton').click()
assert 'Business Dashboard' in driver.page_source
driver.quit()