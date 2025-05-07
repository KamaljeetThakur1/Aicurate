from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get('http://example.com/chat')
    driver.find_element(By.ID, 'question-input').send_keys('    What is the return policy?   ')
    driver.find_element(By.ID, 'send-btn').click()
    assert "Return policy is" in driver.page_source
except Exception as e:
    print(f"Excess spaces handling failed: {e}")
finally:
    driver.quit()