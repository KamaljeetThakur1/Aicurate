from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("chat_interface_url")
driver.find_element(By.ID, "chat_input").send_keys("What is the coverage detail?")
driver.find_element(By.ID, "send_button").click()
assert "Coverage details are as follows:" in driver.page_source
driver.quit()