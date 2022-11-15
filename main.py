from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.netflix.com/in/browse/genre/839338")
driver.find_element("xpath", "/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[2]/a").send_keys(Keys.ENTER)
time.sleep(4)
title = driver.find_element("xpath", "/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/h1")
description = driver.find_element("xpath", "/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]")
print(title.text)
print(description.text)
element = driver.find_element("xpath", "/html/body/div[1]/div/div[2]/section[3]/div[2]/ul/li[1]/div/button")
driver.execute_script("return arguments[0].scrollIntoView();", element)
time.sleep(2)
element.send_keys(Keys.ENTER)
time.sleep(100)