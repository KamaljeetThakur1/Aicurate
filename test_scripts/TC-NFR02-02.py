
# Sample automation script for error handling in reports
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/report')
time.sleep(2)
assert 'No data available for report' in driver.page_source
driver.quit()