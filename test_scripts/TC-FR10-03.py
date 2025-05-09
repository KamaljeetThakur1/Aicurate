from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("chat_interface_url")
driver.find_element(By.ID, "chat_input").send_keys("Tell me about dinosaurs.")
driver.find_element(By.ID, "send_button").click()
assert "I'm sorry, I can't help with that." in driver.page_source
driver.quit()