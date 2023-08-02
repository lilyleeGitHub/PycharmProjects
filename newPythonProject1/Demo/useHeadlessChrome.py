import time

from selenium import webdriver

chrome_options = webdriver.chromeOptions()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../drivers/chromedriver.exe")

driver.get("https://google.com")

print(driver.title)
time.sleep(2)


driver.close()

driver.quit()

time.sleep(2)