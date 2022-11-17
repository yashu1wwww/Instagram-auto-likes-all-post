from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
sleep(4)
driver.find_element_by_name('username').send_keys('dlopoeyg6ygyg') #replace with your insta username
driver.find_element_by_name('password').send_keys('pssesg') #replace with your password
sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(9)
driver.get('https://www.instagram.com/asha.bhat/')
sleep(6)
driver.find_element_by_class_name('_aagw').click()
sleep(2)
driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button').click()
sleep(3)
driver.find_element_by_class_name('_aagw').click()
sleep(5)
driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button').click()
sleep(3)
driver.find_element_by_class_name('_aagw').click()
sleep(5)
driver.find_element_by_xpath('//span[@class="_aamw"]/button/div[2]/span').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button').click()
sleep(3)