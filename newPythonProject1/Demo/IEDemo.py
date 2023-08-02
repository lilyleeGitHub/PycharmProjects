from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

driver=webdriver.Ie()

print(driver.title)

# driver.get("https://google.com")
#
# print(driver.title)
#
# time.sleep(3)
# driver.find_element(By.NAME, "q").send_keys("Yottaa")
# time.sleep(3)
# #
# #
# driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
# time.sleep(2)


driver.close()

driver.quit()