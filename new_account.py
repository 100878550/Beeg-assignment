import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys, ActionChains

class testNewAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://demo.guru99.com")

    @classmethod
    def teardown_method(cls):
        cls.driver.quit()
    
    def test_manager_login(self):
        driver = self.driver
        # driver.find_element(By.NAME, "emailid").send_keys("ManagerTest@gmail.com")
        # driver.find_element(By.NAME, "btnLogin").click()
        # user_id = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(4) td:nth-child(2)").text
        # password = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(5) td:nth-child(2)").text
        driver.get("https://demo.guru99.com/V4/")
        driver.find_element(By.NAME, "uid").send_keys("mngr618426")
        driver.find_element(By.NAME, "password").send_keys("mebedAz")
        driver.find_element(By.NAME, "btnLogin").click()
    
    def test_verify_customer_id(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "New Account").click()

        #NA1
        driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message14").text
        assert "Customer ID is required" in error_message, "Blank Customer ID Error Message Missing"

        #NA2
        driver.find_element(By.NAME, "cusid").send_keys("1234Acc")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Characters are not allowed" in error_message, "Customer ID Character Error Message Missing"

        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Characters are not allowed" in error_message, "Customer ID Character Error Message Missing"

        #NA3
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Special characters are not allowed" in error_message, "Customer ID Special Character Error Message Missing"

        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Special characters are not allowed" in error_message, "Customer ID Special Character Error Message Missing"

        #NA4
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("123 12")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Characters are not allowed" in error_message, "Customer ID Blank Space Error Message Missing"

        #NA5
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys(" ")
        error_message = driver.find_element(By.ID, "message14").text
        assert "First character can not have space" in error_message, "Customer ID First Character Blank Message Missing"

    def test_verify_initial_deposit(self):
        driver = self.driver

        #NA6
        driver.find_element(By.NAME, "inideposit").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message19").text
        assert "Initial Deposit must not be blank" in error_message, "Initial Deposit Blank Message Missing"

        #NA7
        driver.find_element(By.NAME, "inideposit").send_keys("1234Acc")
        error_message = driver.find_element(By.ID, "message19").text
        assert "Characters are not allowed" in error_message, "Initial Deposit Character Error Message Missing"

        driver.find_element(By.NAME, "inideposit").clear()
        driver.find_element(By.NAME, "inideposit").send_keys("Acc123")
        error_message = driver.find_element(By.ID, "message19").text
        assert "Characters are not allowed" in error_message, "Initial Deposit Character Error Message Missing"

        #NA8
        driver.find_element(By.NAME, "inideposit").clear()
        driver.find_element(By.NAME, "inideposit").send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message19").text
        assert "Special characters are not allowed" in error_message, "Initial Deposit Special Character Error Message Missing"

        driver.find_element(By.NAME, "inideposit").clear()
        driver.find_element(By.NAME, "inideposit").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message19").text
        assert "Special characters are not allowed" in error_message, "Initial Deposit Blank Space Error Message Missing"

        #NA9
        driver.find_element(By.NAME, "inideposit").clear()
        driver.find_element(By.NAME, "inideposit").send_keys("123 12")
        error_message = driver.find_element(By.ID, "message19").text
        assert "Characters are not allowed" in error_message, "Initial Deposit First Character Blank Message Missing"
        #NA10
        driver.find_element(By.NAME, "inideposit").clear()
        driver.find_element(By.NAME, "inideposit").send_keys(" ")
        error_message = driver.find_element(By.ID, "message19").text
        assert "First character can not have space" in error_message, "Initial Deposit First Character Blank Message Missing"

    def test_verify_account_type_dropdown(self):
        driver = self.driver

        #NA11
        driver.find_element(By.XPATH, "//select[@name='selaccount']/option[text()='Savings']").click()
        selection = driver.find_element(By.NAME, "selaccount").text
        assert "Savings" in selection, "Savings Selection Error"

        #NA12
        driver.find_element(By.XPATH, "//select[@name='selaccount']/option[text()='Current']").click()
        selection = driver.find_element(By.NAME, "selaccount").text
        assert "Current" in selection, "Savings Selection Error"
    
    def test_reset_button(self):
        driver = self.driver

        #NA13
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("qwer")
        driver.find_element(By.NAME, "reset").click()
        text = driver.find_element(By.NAME, "cusid").text
        assert "" in text, "Reset Button Not Working"

        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("123456")
        driver.find_element(By.NAME, "reset").click()
        text = driver.find_element(By.NAME, "cusid").text
        assert "" in text, "Reset Button Not Working"
        
    def test_submit_button(self):
        customer_id = "618426"
        driver = self.driver

        #NA14 -- brings to blank page
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("123456")
        driver.find_element(By.NAME, "inideposit").send_keys("123456")
        driver.find_element(By.NAME, "button2").click()

        #NA15 -- fails because of blank page jumpscare
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys(customer_id)
        driver.find_element(By.NAME, "inideposit").send_keys("123456")
        driver.find_element(By.NAME, "button2").click()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testNewAccount("test_manager_login"))
    suite.addTest(testNewAccount("test_verify_customer_id"))
    suite.addTest(testNewAccount("test_verify_initial_deposit"))
    suite.addTest(testNewAccount("test_verify_account_type_dropdown"))
    suite.addTest(testNewAccount("test_reset_button"))
    suite.addTest(testNewAccount("test_submit_button"))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
