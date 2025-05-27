
# Sample automation script for invalid code scan
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/scan')
time.sleep(2)
driver.find_element(By.ID, 'scanner').send_keys('InvalidCode')
driver.find_element(By.ID, 'scanButton').click()
assert 'Invalid scan' in driver.page_source
driver.quit()