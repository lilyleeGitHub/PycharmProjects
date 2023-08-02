from selenium import webdriver

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
# time.sleep(2)
driver.implicitly_wait(10)

driver.get("https://google.com")


driver.find_element(By.NAME, "q").send_keys("Yottaa")

driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)

title = driver.title
print(title)

driver.close()
driver.quit()