import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://hatio.in/")

print("STEP 1:", driver.title)

about_us = driver.find_element(By.LINK_TEXT, "About Us")
about_us.click()
print("STEP 2:", driver.title)

culture = driver.find_element(By.LINK_TEXT, "Culture")
culture.click()
print("STEP 3: Culture clicked, new tab opened")

main_window = driver.current_window_handle
handles = driver.window_handles

print("ALL HANDLES:", handles)

for handle in handles:
    if handle != main_window:
        print("SWITCHING TO:", handle)
        driver.switch_to.window(handle)
        break

print("NOW IN TAB:", driver.title)
print("URL:", driver.current_url)

time.sleep(5)
