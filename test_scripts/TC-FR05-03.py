
# Sample automation script for service downtime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/inventory')
time.sleep(2)
# Simulating downtime
disabled = True
if disabled: print('Inventory service is down')
driver.quit()