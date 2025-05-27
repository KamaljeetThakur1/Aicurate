
# Sample automation script for store personnel attributes
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/login')
driver.find_element(By.ID, 'username').send_keys('storeUser')
driver.find_element(By.ID, 'password').send_keys('Password456')
driver.find_element(By.ID, 'loginButton').click()
assert 'Store Dashboard' in driver.page_source
driver.quit()