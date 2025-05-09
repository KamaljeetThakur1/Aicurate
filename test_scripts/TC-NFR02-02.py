from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("chat_interface_url")
for _ in range(3):
driver.find_element(By.ID, "chat_input").send_keys("invalid_query")
driver.find_element(By.ID, "send_button").click()
assert not "Error" in driver.page_source
driver.quit()