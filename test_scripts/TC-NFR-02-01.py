
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_process_policy_question():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://example.com/chat")
    driver.find_element(By.ID, "inputBox").send_keys("What is the code of conduct policy?")
    driver.find_element(By.XPATH, "//button[text()='Send']").click()
    time.sleep(2)
    assert "code of conduct" in driver.page_source
    driver.quit()
