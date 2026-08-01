import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.google.com")
search_box = driver.find_element(By.ID, "APjFqb")
search_box.send_keys("Hello World")
search_box.send_keys(keys.Keys.ENTER)

driver.implicitly_wait(10)

time.sleep(5)