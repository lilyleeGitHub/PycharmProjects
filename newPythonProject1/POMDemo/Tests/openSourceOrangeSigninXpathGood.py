from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest


# class GoogleSearch(unittest.TestCase):
driver = webdriver.Chrome()
time.sleep(2)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


driver.find_element(By.NAME, "username").send_keys("test")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("1234")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("1234")
time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

driver.find_element(By.XPATH, '//*[@id="app"] //*[@class="oxd-form-actions orangehrm-login-action"]').click()
time.sleep(2)
title = driver.title
time.sleep(2)
print(title)

driver.close()
driver.quit()
