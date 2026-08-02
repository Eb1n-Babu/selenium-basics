from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.get("https://www.instagram.com")
driver.get("https://www.facebook.com")

driver.implicitly_wait(10)

driver.back()
driver.back()
