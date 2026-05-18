from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Launch browser
driver = webdriver.Chrome()   # Make sure ChromeDriver is installed and in PATH
driver.maximize_window()

# Step 2: Open demo website
driver.get("https://opensource-demo.orangehrmlive.com/")

# Step 3: Locate username and password fields
username = driver.find_element(By.ID, "txtUsername")
password = driver.find_element(By.ID, "txtPassword")

# Step 4: Enter credentials
username.send_keys("Admin")
password.send_keys("admin123")

# Step 5: Click login button
login_button = driver.find_element(By.ID, "btnLogin")
login_button.click()

# Step 6: Wait to observe result
time.sleep(5)

# Step 7: Close browser
driver.quit()
