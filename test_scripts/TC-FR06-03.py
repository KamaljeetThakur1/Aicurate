from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("chat_interface_url")
driver.find_element(By.ID, "chat_input").send_keys("Tell me the policy details, but do not include everything.")
driver.find_element(By.ID, "send_button").click()
assert "Incomplete query" in driver.page_source
driver.quit()