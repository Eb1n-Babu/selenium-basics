import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.google.com")
by_xpath = driver.find_element(By.XPATH,"//textarea[@name='q']")
by_xpath.send_keys("Hello World")
by_xpath.send_keys(keys.Keys.ENTER)
driver.implicitly_wait(10)
time.sleep(5)
