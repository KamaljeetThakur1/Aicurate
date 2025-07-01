
def filter_invalid_pro_number():
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   try:
       driver.get("https://your-application-url.com/dataset")
       driver.find_element(By.ID, "filterMenu").click()
       driver.find_element(By.ID, "containsCriteria").click()
       driver.find_element(By.ID, "proNumberInput").send_keys("invalid123")
       driver.find_element(By.ID, "applyFilter").click()
       time.sleep(2)
       assert "No results found" in driver.page_source
   finally:
       driver.quit()
