from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/chat')
    driver.find_element(By.ID, 'question-input').send_keys('Hello!')
    driver.find_element(By.ID, 'send-btn').click()
    time.sleep(1)
    assert driver.find_element(By.ID, 'response').is_displayed()
except Exception as e:
    print(f"Responsiveness check failed: {e}")
finally:
    driver.quit()