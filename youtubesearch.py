#Trying to open a browser to youtube to automatically play music

#modules im importing
import selenium, webbrowser, time, pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#step 1: input a song or video you want to find
search = input("Please input a thing you want to search: ")

#step 2: open browser to home page
driver = webdriver.Chrome()
driver.get("http://www.youtube.com")
time.sleep(3)

#step 3:Find and click search box
elemsearch = driver.find_element_by_id("search")
elemsearch.click()

#step 4: send input keys into searchbox
elemsearch.send_keys(search)
elemsearch.send_keys(Keys.RETURN)
time.sleep(2)

#step 5: Identify and click on the first thing
firstresult = driver.find_element_by_partial_link_text(str(search))
firstresult.click()
