from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("chat_interface_url")
driver.find_element(By.ID, "chat_input").send_keys("Where can I find a good pizza?")
driver.find_element(By.ID, "send_button").click()
assert "I cannot respond to that query." in driver.page_source
driver.quit()