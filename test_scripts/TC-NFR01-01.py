from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("chat_interface_url")
start_time = time.time()
assert "Chat Input" in driver.page_source
load_time = time.time() - start_time
assert load_time < 5
driver.quit()