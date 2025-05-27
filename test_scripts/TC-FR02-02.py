
# Sample automation script to test error handling
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/shipping-status')
time.sleep(2)
assert 'Error fetching details' in driver.page_source
driver.quit()