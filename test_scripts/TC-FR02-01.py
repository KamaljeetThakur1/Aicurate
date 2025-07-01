
def apply_date_filter():
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   try:
       driver.get("https://your-application-url.com/data")
       driver.find_element(By.ID, "startDate").send_keys("2023-01-01")
       driver.find_element(By.ID, "endDate").send_keys("2023-01-31")
       driver.find_element(By.ID, "applyFilter").click()
       time.sleep(2)
       assert "Filtered Results" in driver.page_source
   finally:
       driver.quit()
