
# Sample automation script for data fetching error
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/shipping-status')
time.sleep(2)
# Simulate fetch failure
assert 'Error fetching shipping statuses' in driver.page_source
driver.quit()