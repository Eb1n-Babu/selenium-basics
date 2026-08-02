from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click the button that triggers an alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# Switch to alert
alert = driver.switch_to.alert

# Print alert text
print(alert.text)

# Accept the alert
alert.accept()

time.sleep(2)
driver.quit()
