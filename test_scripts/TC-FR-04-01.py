
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_chat_interface_load():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://example.com/chat")
    time.sleep(2)
    assert driver.find_element(By.ID, "inputBox").is_displayed()
    assert driver.title == "Chat Interface"
    driver.quit()
