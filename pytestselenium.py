"""
This is for find particular elements based on elements in a webpage for testing
selenium
"""

from selenium.webdriver.common.by import By

<html>
    <body>
        <form id="loginForm">
            <input name="username" type="text" />
            <input name="password" type="password" />
            <input name="continue" type="submit" value="Login" />
        </form>
    </body>
</html>

login_form = driver.find_element_by_id('loginForm')
username = driver.find_element_by_name('username')
password = driver,find_element_by_name('password')

continue = driver.find_element_by_name('continue')

login_form = driver.find_element_by_xpath("/html/body/form[1]")
login_form = driver.find_element_by_xpath("//form[1]")
login_form = driver.find_element_by_xpath("//form[@id='loginForm']")

username = driver.find_element_by_xpath("//form[input/@name='username']")
username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
username = driver.find_element_by_xpath("//input[@name='username']")
