import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.set_page_load_timeout(10)

driver.get("https://google.com")

# driver.find_element_by_name("q").send_keys("Automation step by sy step")
time.sleep(3)
driver.find_element(By.NAME, "q").send_keys("Yottaa")
time.sleep(3)


driver.find_element(By.NAME, "btnK").click()
# driver.find_element(By.XPATH("//input[@name='btnk']")).click()

time.sleep(3)

driver.close()

driver.quit()

print("test completed")