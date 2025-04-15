import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException

class testDeleteAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://demo.guru99.com")

    @classmethod
    def teardown_method(cls):
        cls.driver.quit()
    
    def test_manager_login(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/")
        driver.find_element(By.NAME, "uid").send_keys("mngr618426")
        driver.find_element(By.NAME, "password").send_keys("mebedAz")
        driver.find_element(By.NAME, "btnLogin").click()

    def create_customer(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "New Customer").click()
        driver.find_element(By.NAME, "name").send_keys("TestCustomer")
        driver.find_element(By.NAME, "dob").send_keys("1999" + Keys.TAB + "1023")
        driver.find_element(By.NAME, "addr").send_keys("123 Street")
        driver.find_element(By.NAME, "city").send_keys("Test City")
        driver.find_element(By.NAME, "state").send_keys("Test State")
        driver.find_element(By.NAME, "pinno").send_keys("123456")
        driver.find_element(By.NAME, "telephoneno").send_keys("123")
        driver.find_element(By.NAME, "emailid").send_keys("test@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("123")
        driver.find_element(By.NAME, "sub").click()
        time.sleep(3)

    def test_create_account(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "New Account").click()
        driver.find_element(By.NAME, "cusid").send_keys("41122")
        driver.find_element(By.NAME, "selaccount").send_keys("Current")
        driver.find_element(By.NAME, "inideposit").send_keys("1000")
        driver.find_element(By.NAME, "button2").click()
        time.sleep(3)

    def test_verify_account_number(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Delete Account").click()

        # DA1
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message2").text
        assert "Account Number must not be blank" in error_message

        # DA2
        driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Characters are not allowed" in error_message

        # DA3
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Special characters are not allowed" in error_message

        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Special characters are not allowed" in error_message

        # DA4
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123 12")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Characters are not allowed" in error_message

        # DA5
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(" ")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Characters are not allowed" in error_message

    def test_verify_submit_button(self):
        driver = self.driver

        # DA6 - valid account, may or may not exist
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("144234")
        driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(1)

        try:
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(1)
            alert = driver.switch_to.alert
            alertText = alert.text
            alert.accept()
            assert "Account deleted successfully" in alertText or "Account does not exist" in alertText
        except NoAlertPresentException:
            self.fail("Expected alert after submitting account number not found.")

        # DA7 - re-delete same account
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("144234")
        driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(1)
        try:
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(1)
            alert = driver.switch_to.alert
            alertText = alert.text
            alert.accept()
            assert "Account does not exist" in alertText
        except NoAlertPresentException:
            self.fail("Expected alert after re-submitting deleted account.")

    def test_verify_reset_button(self):
        driver = self.driver

        # DA8
        field = driver.find_element(By.NAME, "accountno")
        field.clear()
        field.send_keys("qwer")
        driver.find_element(By.NAME, "res").click()
        text_field = field.get_attribute("value")
        assert text_field == "", "Text not reset properly"

        field.send_keys("123456")
        driver.find_element(By.NAME, "res").click()
        text_field = field.get_attribute("value")
        assert text_field == "", "Text not reset properly"

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testDeleteAccount("test_manager_login"))
    suite.addTest(testDeleteAccount("test_create_account"))
    suite.addTest(testDeleteAccount("test_verify_account_number"))
    suite.addTest(testDeleteAccount("test_verify_submit_button"))
    suite.addTest(testDeleteAccount("test_verify_reset_button"))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
