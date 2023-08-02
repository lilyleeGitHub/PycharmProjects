import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--disable-extensions")
#
path = "../drivers/geckodriver.exe"

driver = webdriver.Firefox(executable_path=path,firefox_options=firefox_options)

#driver = webdriver.Firefox()




# driver.set_page_load_timeout(10)

driver.get("https://google.com")

#driver.find_element_by_name("q").send_keys("Automation step by sy step")
# time.sleep(3)
driver.find_element(By.NAME, "q").send_keys("Yottaa")
time.sleep(3)
#
#
driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
# # driver.find_element(By.XPATH("//input[@name='btnk']")).click()
#
# time.sleep(3)

driver.close()

driver.quit()

print("test completed")