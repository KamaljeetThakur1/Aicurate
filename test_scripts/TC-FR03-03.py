
# Sample automation script for scanner downtime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://webapp.com/scan')
time.sleep(2)
# Simulating downtime
disabled = True
if disabled: print('Scanner is down')
driver.quit()