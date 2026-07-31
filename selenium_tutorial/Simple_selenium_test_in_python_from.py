import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://google.com")
driver.maximize_window()
driver.find_element(By.ID,"SIvCob").find_element(By.XPATH,"//a[text()='English']").click()
#driver.find_element(By.XPATH, "//div[@id='SIvCob']//a[text()='English']").click()
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("English")
search_box.send_keys(keys.Keys.ENTER)
time.sleep(5)