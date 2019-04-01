"""
This is studying waits in selenium
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebdriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/Url_that_delays_loading")
try:
    element = WebdriverWait(driver, 10).until(
        EC.prescence_of_element_located((By.ID, "mydynamicElement"))
    )
finally:
    driver.quit()
