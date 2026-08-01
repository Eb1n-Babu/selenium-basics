import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.google.com")
by_tag_name = driver.find_element(By.TAG_NAME, "textarea")
by_tag_name.send_keys("test")
by_tag_name.send_keys(Keys.ENTER)

driver.implicitly_wait(10)
time.sleep(5)