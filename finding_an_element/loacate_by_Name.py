import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.google.com")
by_name =  driver.find_element(By.NAME, "q")
by_name.send_keys("Hello World")
by_name.send_keys(keys.Keys.ENTER)
driver.implicitly_wait(10)

time.sleep(5)
