from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def filter_pro_number(driver):
    try:
        wait = WebDriverWait(driver, 15)
        pro_number_filter = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/main/div/div[2]/div[2]/div/table/thead/tr/th[1]/button')))
        pro_number_filter.click()
        operator_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[3]/ul/div/div[1]/div/div[2]/div/div")))
        operator_dropdown.click()

        contains_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Contains')]")))
        contains_option.click()
        value_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="filled-basic"]')))
        value_input.clear()
        value_input.send_keys("63")

        # Click on the Filter button
        filter_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/ul/div/div[3]/button[2]')))
        filter_button.click()

        time.sleep(5) 
        print("PRO Number filter applied successfully.")

    except Exception as e:
        print(f"Error in Test Case 3 (PRO Number Filter): {e}")
