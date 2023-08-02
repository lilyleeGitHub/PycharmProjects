from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# class GoogleSearch(unittest.TestCase):
driver = webdriver.Chrome()
time.sleep(2)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://google.com")


driver.find_element(By.NAME, "q").send_keys("Yottaa")

driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)

title = driver.title
print(title)

driver.close()
driver.quit()
