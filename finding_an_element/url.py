import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

#opening url
driver = webdriver.Chrome()
driver.get("https://google.com")

x = driver.find_element(By.NAME,"q")
x.send_keys("hello")
#x.clear()
x.send_keys(Keys.ENTER)

#refresh
driver.refresh()
time.sleep(5)