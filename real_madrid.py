from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config

browser = webdriver.Firefox()
browser.get("https://dcbookstore.com/")
browser.implicitly_wait(5)
browser.maximize_window()

element = browser.find_element(By.LINK_TEXT, "Login")
element.click()

username = browser.find_element(By.NAME,"email")
username.send_keys(config("EMAIL"))

password = browser.find_element(By.NAME,"password")
password.send_keys(config("PASSWORD"))

login_button = browser.find_element(By.CLASS_NAME,"blulogin")
login_button.click()

drop_down = browser.find_element(By.CLASS_NAME,"pull-right")
drop_down.click()

order = browser.find_element(By.LINK_TEXT,"My Orders")
order.click()

browser.implicitly_wait(50000)

