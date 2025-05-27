
# Sample automation script for partial data handling
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/shipping-status')
time.sleep(2)
assert 'Partial data retrieved' in driver.page_source
driver.quit()