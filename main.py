from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
username = 'YOURUSERNAME'
password = 'YOURPASSWORD'
driver = webdriver.YOURBROWSER(executable_path='YOUR WEBDRIVER PATH')

driver.get("https://scratch.mit.edu/login")
sleep(3)
driver.find_element_by_id('id_username').click()
driver.find_element_by_id('id_username').send_keys(username)
driver.find_element_by_id('id_password').send_keys(password)
driver.find_element_by_id('id_password').send_keys(Keys.RETURN)

sleep(3)

sleep(5)

for i in range(5):
    driver.get('https://scratch.mit.edu/explore/projects/all/recent')
    sleep(1)
    driver.find_element_by_class_name("thumbnail-image").click()
    driver.find_element_by_class_name("inplace-textarea").click()
    driver.find_element_by_class_name("inplace-textarea").send_keys('Nice Project!')
    driver.find_element_by_class_name("compose-post").click()
    sleep(10)
