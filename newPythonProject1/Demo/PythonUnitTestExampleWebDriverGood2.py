import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome()
        print("webdriver object" + str(cls.driver))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()

    def test_search(self):
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME, "q").send_keys("Yottaa")
        time.sleep(3)
        self.driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
        time.sleep(2)
        title = self.driver.title
        print("title " + title)
        self.assertEqual(title, "Yottaa - Google Search")

    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

# if __name__ == '__main__':
#     unittest.main()