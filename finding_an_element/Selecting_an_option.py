import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://www.webapp.ceo.kerala.gov.in/detailedResults.html?lang=en")
government = Select(driver.find_element(By.ID,'distNo'))
government.select_by_visible_text("2.KANNUR")
driver.implicitly_wait(5)
time.sleep(5)

"""select_by_index(index)
This method takes an integer value which is the index of the option that we intend to select.
select_by_visible_text(“text”)
This method takes a string value and selects the option that is displaying the same text.
select_by_value(value)
This method takes a string value and selects an option with the same value attribute.
deselect_all()
This method lets you deselect all the selected options.
"""
