from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def apply_date_filter(driver, start_date_label, end_date_label):
    """
    Applies expected delivery date filter by selecting start and end dates using the calendar picker.
    """
    wait = WebDriverWait(driver, 15)

    try:
        start_date_svg = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div/div/main/div/div[1]/div[2]/div[2]/div[1]/div/div/div/button')
        ))
        start_date_svg.click()
        start_date_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/button[4]'))
        )
        start_date_element.click()

        time.sleep(5)

        end_date_svg = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div/div/main/div/div[1]/div[2]/div[2]/div[2]/div/div/div/button')
        ))
        end_date_svg.click()
        end_date_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/button[6]'))
        )
        end_date_element.click()

        time.sleep(5)

        ok_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'OK')]")
        ))
        ok_button.click()

        clear_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div/main/div/div[2]/div[2]/div[2]/button'))
        )
        clear_button.click()

        time.sleep(5)  
        print("Date filter test case completed successfully.")

    except Exception as e:
        print(f"Error during date filter test case: {e}")
