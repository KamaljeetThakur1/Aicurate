from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("chat_interface_url")
driver.find_element(By.ID, "chat_input").send_keys("What is the policy on holidays?!")
driver.find_element(By.ID, "send_button").click()
assert "Policy on holidays" in driver.page_source
driver.quit()