import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.alert import Alert

class testCustomisedStatement(unittest.TestCase):
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
        driver.find_element(By.LINK_TEXT, "Customised Statement").click()

        #CS1
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message2").text
        assert "Account Number must not be blank" in error_message, "Acount Number Blank Error Message Missing"

        #CS2
        driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Characters are not allowed" in error_message, "Acount Number Character Error Message Missing"

        #CS3
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Special characters are not allowed" in error_message, "Acount Number Special Character Error Message Missing"

        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Special characters are not allowed" in error_message, "Acount Number Special Character Error Message Missing"

        #CS4
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123 12")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Characters are not allowed" in error_message, "Acount Number First Space Blank Error Message Missing"

        #CS5
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(" ")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Characters are not allowed" in error_message, "Acount Number First Space Blank Error Message Missing"
    
    def verify_from_date_field(self):
        driver = self.driver
        #CS6
        driver.find_element(By.NAME, "fdate").send_keys("")
        error_message = driver.find_element(By.ID, "message26").text
        assert "From Date Field must not be blank" in error_message, "From Date Blank Error Message Missing"

    def verify_to_date_field(self):
        driver = self.driver
        #CS7
        driver.find_element(By.NAME, "tdate").send_keys("")
        driver.find_element(By.NAME, "accountno").send_keys("")
        error_message = driver.find_element(By.ID, "message27").text
        assert "To Date Field must not be blank" in error_message, "To Date Blank Error Message Missing"
    
    def verify_minimum_transaction_value(self):
        driver = self.driver
        #CS8
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("Acc123")
        error_message = driver.find_element(By.ID, "message12").text
        assert "Characters are not allowed" in error_message, "Minimum Transaction Value Character Error Message Missing"

        #CS9
        driver.find_element(By.NAME, "amountlowerlimit").clear()
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message12").text
        assert "Special characters are not allowed" in error_message, "Minimum Transaction Value Special Character Error Message Missing"

        driver.find_element(By.NAME, "amountlowerlimit").clear()
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message12").text
        assert "Special characters are not allowed" in error_message, "Minimum Transaction Value Special Character Error Message Missing"

        #CS10
        driver.find_element(By.NAME, "amountlowerlimit").clear()
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("123 12")
        error_message = driver.find_element(By.ID, "message12").text
        assert "Characters are not allowed" in error_message, "Minimum Transaction Value First Space Blank Error Message Missing"

        #CS11
        driver.find_element(By.NAME, "amountlowerlimit").clear()
        driver.find_element(By.NAME, "amountlowerlimit").send_keys(" ")
        error_message = driver.find_element(By.ID, "message12").text
        assert "Characters are not allowed" in error_message, "Minimum Transaction Value First Space Blank Error Message Missing"

    def verify_number_of_transaction(self):
        driver = self.driver
        #CS12
        driver.find_element(By.NAME, "numtransaction").send_keys("Acc123")
        error_message = driver.find_element(By.ID, "message13").text
        assert "Characters are not allowed" in error_message, "Number Of Transaction Character Error Message Missing"

        #CS13
        driver.find_element(By.NAME, "numtransaction").clear()
        driver.find_element(By.NAME, "numtransaction").send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message13").text
        assert "Special characters are not allowed" in error_message, "Number Of Transaction Special Character Error Message Missing"

        driver.find_element(By.NAME, "numtransaction").clear()
        driver.find_element(By.NAME, "numtransaction").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message13").text
        assert "Special characters are not allowed" in error_message, "Number Of Transaction Special Character Error Message Missing"

        #CS14
        driver.find_element(By.NAME, "numtransaction").clear()
        driver.find_element(By.NAME, "numtransaction").send_keys("123 12")
        error_message = driver.find_element(By.ID, "message13").text
        assert "Characters are not allowed" in error_message, "Number Of Transaction First Space Blank Error Message Missing"

        #CS15
        driver.find_element(By.NAME, "numtransaction").clear()
        driver.find_element(By.NAME, "numtransaction").send_keys(" ")
        error_message = driver.find_element(By.ID, "message13").text
        assert "Characters are not allowed" in error_message, "Number Of Transaction First Space Blank Error Message Missing"
    
    def reset_button(self):
        driver = self.driver
        #CS16
        driver.find_element(By.NAME, "accountno").send_keys("1")
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("2")
        driver.find_element(By.NAME, "numtransaction").send_keys("3")
        driver.find_element(By.NAME, "res").click()
        text = driver.find_element(By.NAME, "accountno").text
        assert "" in text, "Reset Button Does Not Work"
        text = driver.find_element(By.NAME, "amountlowerlimit").text
        assert "" in text, "Reset Button Does Not Work"
        text = driver.find_element(By.NAME, "numtransaction").text
        assert "" in text, "Reset Button Does Not Work"

    def submit_button(self):
        driver = self.driver
        #CS17 -- dont have account number
        driver.find_element(By.NAME, "accountno").send_keys("123")
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("100")
        driver.find_element(By.NAME, "numtransaction").send_keys("50")
        driver.find_element(By.NAME, "fdate").send_keys("1995" + Keys.TAB + "1124")
        driver.find_element(By.NAME, "tdate").send_keys("1999" + Keys.TAB + "1124")
        alert = driver.switch_to.alert
        alertText = alert.text
        alert.accept()
        assert "Account does not exist" in alertText, "InValid Acount Number Error Message Missing"


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testCustomisedStatement("manager_login"))
    suite.addTest(testCustomisedStatement("verify_account_number"))
    suite.addTest(testCustomisedStatement("verify_from_date_field"))
    suite.addTest(testCustomisedStatement("verify_to_date_field"))
    suite.addTest(testCustomisedStatement("verify_minimum_transaction_value"))
    suite.addTest(testCustomisedStatement("verify_number_of_transaction"))
    suite.addTest(testCustomisedStatement("reset_button"))
    suite.addTest(testCustomisedStatement("submit_button"))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)