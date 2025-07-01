
def filter_by_pro_number():
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   try:
       driver.get("https://your-application-url.com/dataset")
       driver.find_element(By.ID, "filterMenu").click()
       driver.find_element(By.ID, "containsCriteria").click()
       driver.find_element(By.ID, "proNumberInput").send_keys("12345")
       driver.find_element(By.ID, "applyFilter").click()
       time.sleep(2)
       assert "Filtered Results" in driver.page_source
   finally:
       driver.quit()
