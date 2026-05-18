import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("https://iqvia.wd1.myworkdayjobs.com/IQVIA/login")
browser.maximize_window()

time.sleep(5)

username = browser.find_element(By.CLASS_NAME, "css-15rz5ap").find_element(By.ID, "input-4")
username.send_keys("hello")
passwords = browser.find_element(By.CLASS_NAME, "css-1kxrhf3").find_element(By.ID, "input-5")
passwords.send_keys("dddd")

time.sleep(5)