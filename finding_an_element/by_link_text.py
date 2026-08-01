import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.google.com")
driver.find_element(By.LINK_TEXT,"English").click()
driver.find_element(By.XPATH,"//a[contains(text(),'हिन्दी')]").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Eng").click()
driver.implicitly_wait(10)
time.sleep(5)

xy = driver.find_elements(By.NAME,"q")
print(xy)

#ID = :"id"
#XPATH = “xpath”
#NAME = “name”
#TAG_NAME = “tag name”
#CLASS_NAME = “class name”
#LINK_TEXT = “link text”
#PARTIAL_LINK_TEXT = “partial link text”

"""
find_element
– It returns the first instance from multiple web elements with a 
particular attribute in theDOM. 
The method throws NoSuchElementException if no web elements are matching 
the required web locator. 

find_elements
– It returns a list of all the instances of WebElements matching a particular attribute. 
The list is empty in case there are no matching elements in the DOM.
"""