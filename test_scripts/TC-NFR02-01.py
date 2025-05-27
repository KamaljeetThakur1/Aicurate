
# Sample automation script for dashboard layout
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/dashboard')
time.sleep(2)
assert 'Dashboard' in driver.title
assert driver.find_element(By.ID, 'monthlyReports').is_displayed()
driver.quit()