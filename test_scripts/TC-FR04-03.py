
# Sample automation script for heavy data load
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/dashboard')
time.sleep(2)
# Assume data gets loaded here
assert 'Data loaded successfully' in driver.page_source
driver.quit()