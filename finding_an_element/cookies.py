import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com/")
driver.save_screenshot("lambdatest.png")
cookies = {'name' : 'user', 'value' : 'vinayak'}
driver.add_cookie(cookies)

x = driver.get_cookies()
driver.set_window_size(1200,899)
print(x)
time.sleep(5)

"""Explicit Wait tells Selenium to wait for a specific condition to 
happen before moving to the next step.Wait for all elements, globally."""

#driver.implicitly_wait(10)
#One-line definitions (super short)
#Explicit Wait: Wait until a specific condition is true.

#Implicit Wait: Wait a fixed time for all element searches.