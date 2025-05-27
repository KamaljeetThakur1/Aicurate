
# Sample automation script for real-time visibility
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/shipping-status')
time.sleep(2)
assert 'Shipping Status' in driver.page_source
# Assume change happens in the backend
driver.quit()