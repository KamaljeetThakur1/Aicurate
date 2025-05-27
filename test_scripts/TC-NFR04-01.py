
# Sample automation script for monitoring tool verification
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/monitoring')
assert 'Infrastructure Monitoring' in driver.title
assert driver.find_element(By.ID, 'cpuUsage').is_displayed()
driver.quit()