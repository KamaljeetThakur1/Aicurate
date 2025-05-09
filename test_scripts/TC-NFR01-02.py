from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("chat_interface_url")
assert "Interface Error" in driver.page_source
driver.quit()