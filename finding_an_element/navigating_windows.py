import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://hatio.in/")

print("STEP 1:", driver.title)

# Click About Us (same tab)
about_us = driver.find_element(By.LINK_TEXT, "About Us")
about_us.click()
print("STEP 2:", driver.title)

# Open Culture in NEW TAB using CTRL + ENTER
culture = driver.find_element(By.LINK_TEXT, "Culture")
culture.send_keys(Keys.CONTROL + Keys.RETURN)
print("STEP 3: Culture opened in NEW TAB")

time.sleep(2)

# Print handles BEFORE switching
print("WINDOW HANDLES BEFORE SWITCH:", driver.window_handles)

main_window = driver.current_window_handle

# Switch to the new tab
for handle in driver.window_handles:
    if handle != main_window:
        print("SWITCHING TO:", handle)
        driver.switch_to.window(handle)
        break

# Print details AFTER switching
print("NOW IN TAB:", driver.title)
print("URL:", driver.current_url)

time.sleep(5)
driver.quit()
