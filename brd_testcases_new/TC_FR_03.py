from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def filter_pro_number(driver):
    """
    Applies PRO number filter with improved error handling and stability.
    """
    try:
        wait = WebDriverWait(driver, 20)
        actions = ActionChains(driver)
        
        time.sleep(2)
        pro_number_filter = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div/div/main/div/div[2]/div[2]/div/table/thead/tr/th[1]/button')
        ))
        
        # Scroll element into view
        driver.execute_script("arguments[0].scrollIntoView(true);", pro_number_filter)
        time.sleep(1)
        
        # Try multiple click methods
        try:
            pro_number_filter.click()
        except:
            driver.execute_script("arguments[0].click();", pro_number_filter)
        
        # Wait for filter dropdown to appear
        time.sleep(2)
        
        operator_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/div[3]/ul/div/div[1]/div/div[2]/div/div")
        ))
        
        driver.execute_script("arguments[0].scrollIntoView(true);", operator_dropdown)
        time.sleep(1)
        
        try:
            operator_dropdown.click()
        except:
            driver.execute_script("arguments[0].click();", operator_dropdown)
        time.sleep(2)

        contains_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[contains(text(), 'Contains')]")
        ))
        
        driver.execute_script("arguments[0].scrollIntoView(true);", contains_option)
        time.sleep(1)
        
        try:
            contains_option.click()
        except:
            driver.execute_script("arguments[0].click();", contains_option)
        time.sleep(2)
        value_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="filled-basic"]')
        ))

        driver.execute_script("arguments[0].scrollIntoView(true);", value_input)
        value_input.clear()
        time.sleep(1)
        
        try:
            value_input.send_keys("63")
        except:
            try:
                value_input.click()
                time.sleep(1)
                value_input.clear()
                value_input.send_keys("63")
            except:
                driver.execute_script("arguments[0].value = '63';", value_input)
                driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", value_input)
        
        time.sleep(2)
        filter_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div[3]/ul/div/div[3]/button[2]')
        ))
        
        driver.execute_script("arguments[0].scrollIntoView(true);", filter_button)
        time.sleep(1)
        
        try:
            filter_button.click()
        except:
            driver.execute_script("arguments[0].click();", filter_button)
        time.sleep(5)
        print("PRO Number filter applied successfully.")

    except Exception as e:
        print(f"Error in Test Case 3 (PRO Number Filter): {e}")
        
        try:
            actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
        except:
            pass
        try:
            driver.execute_script("document.body.click();")
            time.sleep(1)
        except:
            pass