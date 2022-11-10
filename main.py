from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.netflix.com/in/login")
driver.find_element("name", "userLoginId").send_keys(os.environ['email'])
driver.find_element("name", "password").send_keys(os.environ['password'])
driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div/div[1]/form/button").send_keys(Keys.ENTER)
time.sleep(4)
driver.find_element("link_text", "General").click()
driver.find_element("link_text", "Suits").click()
time.sleep(4)
