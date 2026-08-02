from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_height_width")

print("Page loaded:", driver.title)

# STEP 1: Switch to the main iframe (the result frame)
driver.switch_to.frame("iframeResult")

print("Inside first iframe!")

# STEP 2: Now switch to the inner iframe
inner_iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(inner_iframe)

print("Inside second iframe!")

# STEP 3: Read text inside the inner iframe
text = driver.find_element(By.TAG_NAME, "h1").text
print("Text inside inner iframe:", text)

time.sleep(3)

# STEP 4: Go back to first iframe
driver.switch_to.parent_frame()
print("Back to first iframe")

# STEP 5: Go back to main page
driver.switch_to.default_content()
print("Back to main page:", driver.title)

driver.quit()
