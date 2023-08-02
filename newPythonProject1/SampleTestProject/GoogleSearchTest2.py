import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        time.sleep(2)

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_yottaa(self):
        self.driver.get("https://google.com")

        self.driver.find_element(By.NAME, "q").send_keys("Yottaa")

        self.driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)

        title = self.driver.title
        print(title)



    # def tearDown(cls) -> None:
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

# if __name__ == '__main__':
#     unittest.main()
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Pear3\\PycharmProjects\\newPythonProject1\\Demo\\testOutput"))
