import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


class testBalanceEnquiry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://demo.guru99.com/V4/")
        cls.driver.find_element(By.NAME, "uid").send_keys("mngr618426")
        cls.driver.find_element(By.NAME, "password").send_keys("mebedAz")
        cls.driver.find_element(By.NAME, "btnLogin").click()

    @classmethod
    def tearDownClass(cls):  # fixed teardown method name
        cls.driver.quit()

    def go_to_balance_enquiry(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "accountno"))
        )

    def test_verify_account_number(self):
        driver = self.driver
        self.go_to_balance_enquiry()

        # BE1 - blank
        account_input = driver.find_element(By.NAME, "accountno")
        account_input.send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message2").text
        self.assertIn("Account Number must not be blank", error_message)

        # BE2 - characters
        account_input.send_keys("Acc123")
        error_message = driver.find_element(By.ID, "message2").text
        self.assertIn("Characters are not allowed", error_message)

        # BE3 - special characters
        account_input.clear()
        account_input.send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message2").text
        self.assertIn("Special characters are not allowed", error_message)

        account_input.clear()
        account_input.send_keys("!@#")
        error_message = driver.find_element(By.ID, "message2").text
        self.assertIn("Special characters are not allowed", error_message)

        # BE4 - space
        account_input.clear()
        account_input.send_keys(" ")
        error_message = driver.find_element(By.ID, "message2").text
        self.assertIn("Characters are not allowed", error_message)

    def test_verify_submit_button(self):
        driver = self.driver
        self.go_to_balance_enquiry()

        # BE5
        account_input = driver.find_element(By.NAME, "accountno")
        account_input.clear()
        account_input.send_keys("123456")
        driver.find_element(By.NAME, "AccSubmit").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alertText = alert.text
        alert.accept()
        self.assertIn("Account does not exist", alertText)

        # BE6 - again
        self.go_to_balance_enquiry()
        account_input = driver.find_element(By.NAME, "accountno")
        account_input.clear()
        account_input.send_keys("123456")
        driver.find_element(By.NAME, "AccSubmit").click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alertText = alert.text
        alert.accept()
        self.assertIn("Account does not exist", alertText)

    def test_verify_reset_button(self):
        driver = self.driver
        self.go_to_balance_enquiry()

        # BE7
        account_input = driver.find_element(By.NAME, "accountno")
        account_input.send_keys("qwer")
        driver.find_element(By.NAME, "res").click()
        text_value = account_input.get_attribute("value")
        self.assertEqual(text_value, "", "Text not reset after input 'qwer'")

        account_input.send_keys("123456")
        driver.find_element(By.NAME, "res").click()
        text_value = account_input.get_attribute("value")
        self.assertEqual(text_value, "", "Text not reset after input '123456'")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testBalanceEnquiry("test_verify_account_number"))
    suite.addTest(testBalanceEnquiry("test_verify_submit_button"))
    suite.addTest(testBalanceEnquiry("test_verify_reset_button"))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
