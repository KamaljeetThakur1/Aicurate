
# Sample automation script for no data condition
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/dashboard')
time.sleep(2)
assert 'No data available' in driver.page_source
driver.quit()