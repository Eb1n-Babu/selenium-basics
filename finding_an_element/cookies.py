import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com/")
cookies = {'name' : 'user', 'value' : 'vinayak'}
driver.add_cookie(cookies)

x = driver.get_cookies()
driver.set_window_size(1200,899)
print(x)
time.sleep(5)