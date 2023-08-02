

from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import sys
import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "...","..."))
# # sys.path.append('C:/Users/Pear3/PycharmProjects/newPythonProject1')
# sys.path.append('.')
from newPythonProject1.POMDemo.Pages.loginPage import LoginPage



class LoginTests(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome()
        time.sleep(2)
        cls.driver.implicitly_wait(10)

    def test_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://facebook.com")

        login = LoginPage(driver)
        login.enter_username("Test")
        login.enter_password("1234")
        # login.click_login()


        # self.driver.find_element(By.ID, "email").send_keys("test")
        # time.sleep(2)
        # self.driver.find_element(By.ID, "pass").send_keys("1234")
        # time.sleep(2)
        self.driver.find_element(By.NAME, "login").click()
        time.sleep(2)


        # self.driver.find_element(By.XPATH, '//*[@id="app"] //*[@class="oxd-form-actions orangehrm-login-action"]').click()
        time.sleep(2)
        title = self.driver.title
        time.sleep(2)
        print(title)



    @classmethod
    def tearDown(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


# if __name__ == '__main__':
#     unittest.main()
