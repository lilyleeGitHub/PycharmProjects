import time

from selenium import webdriver

driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.get("https://google.com")

print(driver.title)
time.sleep(2)


driver.close()

driver.quit()

time.sleep(2)

print("test completed")