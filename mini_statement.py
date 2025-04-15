import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.alert import Alert

class testMiniStatement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://demo.guru99.com")

    @classmethod
    def teardown_method(cls):
        cls.driver.quit()
    
    def manager_login(self):
        driver = self.driver
        # driver.find_element(By.NAME, "emailid").send_keys("ManagerTest@gmail.com")
        # driver.find_element(By.NAME, "btnLogin").click()
        # user_id = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(4) td:nth-child(2)").text
        # password = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(5) td:nth-child(2)").text
        driver.get("https://demo.guru99.com/V4/")
        driver.find_element(By.NAME, "uid").send_keys("mngr618426")
        driver.find_element(By.NAME, "password").send_keys("mebedAz")
        driver.find_element(By.NAME, "btnLogin").click()

    def verify_account_number(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Mini Statement").click()

        #MS1
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message2").text
        assert "Account Number must not be blank" in error_message, "Blank Account Number Error Message Missing"

        #MS2
        driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Characters are not allowed" in error_message, "Account Number Character Error Message Missing" 

        #MS3
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Special characters are not allowed" in error_message, "Account Number Special Character Error Message Missing"

        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Special characters are not allowed" in error_message, "Account Number Special Character Error Message Missing"

        #MS4
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123 12")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Characters are not allowed" in error_message, "Account Number Blank Space Error Message Missing"

        #MS5
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(" ")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Characters are not allowed" in error_message, "Account Number First Space Blank Error Message Missing"

    def verify_submit_button(self):
        driver = self.driver

        #MS6 -- wasnt able to create account so dont have valid account
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123456")
        driver.find_element(By.NAME, "AccSubmit").click()
        alert = driver.switch_to.alert
        alert.accept()
        alert = driver.switch_to.alert
        alertText = alert.text
        alert.accept()
        assert "Account deleted successfully" in alertText, "Valid Account Submit Not Working"
        #MS7
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123456")
        driver.find_element(By.NAME, "AccSubmit").click()
        alert = driver.switch_to.alert
        alert.accept()
        alert = driver.switch_to.alert
        alertText = alert.text
        alert.accept()
        assert "Account does not exist" in alertText, "Invalid Account Submit Not Working"

    def verify_reset_button(self):
        driver = self.driver
        #MS8
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("qwer")
        driver.find_element(By.NAME, "res").click()
        text_field = driver.find_element(By.NAME, "accountno").text

        assert "" in text_field, "Text Not Reset"

     
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123456")
        driver.find_element(By.NAME, "res").click()
        text_field = driver.find_element(By.NAME, "accountno").text

        assert "" in text_field, "Text Not Reset"







if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testMiniStatement("manager_login"))
    suite.addTest(testMiniStatement("verify_account_number"))
    suite.addTest(testMiniStatement("verify_submit_button"))
    suite.addTest(testMiniStatement("verify_reset_button"))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)