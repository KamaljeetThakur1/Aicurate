
# Sample automation script for data mismatch
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/inventory')
time.sleep(2)
assert 'Data mismatch' in driver.page_source
driver.quit()