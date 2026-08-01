import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.google.com")
driver.find_element(By.LINK_TEXT,"English").click()
driver.find_element(By.XPATH,"//a[contains(text(),'हिन्दी')]").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Eng").click()
driver.implicitly_wait(10)
time.sleep(5)
