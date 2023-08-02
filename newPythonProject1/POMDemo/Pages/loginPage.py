from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id ="email"
        self.password_textbox_id = "pass"

        self.login_button_id = "u_0_5_fT"

    def enter_username(self,username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):

        self.driver.find_element(By.ID, self.login_button_id).click()


