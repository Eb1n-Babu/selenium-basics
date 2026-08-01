import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.google.com")
class_element = driver.find_element(By.CLASS_NAME,"gLFyf")
class_element.send_keys("Hello World")
class_element.send_keys(keys.Keys.ENTER)
time.sleep(5)