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
    def test_create_customer(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "New Customer").click()
        driver.find_element(By.NAME, "name").send_keys("TestCustomer")
        driver.find_element(By.NAME, "dob").send_keys("1999" + Keys.TAB + "1023")
        driver.find_element(By.NAME, "addr").send_keys("123 Street")
        driver.find_element(By.NAME, "city").send_keys("Test City")
        driver.find_element(By.NAME, "state").send_keys("Test State")
        driver.find_element(By.NAME, "pinno").send_keys("123456")
        driver.find_element(By.NAME, "telephoneno").send_keys("123")
        driver.find_element(By.NAME, "emailid").send_keys("TestCustomer5d2er994@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("123")
        driver.find_element(By.NAME, "sub").click()
        time.sleep(1)
        global customer_id
        customer_id = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(4) td:nth-child(2)").text

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
        customer_id = "51758"
        driver = self.driver

        #NA14 
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("123456789")
        driver.find_element(By.NAME, "inideposit").send_keys("123456")
        driver.find_element(By.NAME, "button2").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alertText = alert.text
        alert.accept()
        assert "Customer does not exist!!" in alertText, "not work"

        #NA15 
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys(customer_id)
        driver.find_element(By.NAME, "inideposit").send_keys("123456")
        driver.find_element(By.NAME, "button2").click()
        time.sleep(2)
        text = driver.find_element(By.XPATH,"/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/p[1]").text
        
        assert "Account Generated Successfully!!!" in text, "bad"
        
    def test_next_page(self):
        driver = self.driver
        #NA16
        driver.find_element(By.LINK_TEXT, "Continue").click()
        text = driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/marquee").text
        assert "Welcome To Manager's Page of Guru99 Bank" in text, "Continue button did not work"



if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testNewAccount("test_manager_login"))
    # suite.addTest(testNewAccount("test_create_customer"))
    suite.addTest(testNewAccount("test_verify_customer_id"))
    suite.addTest(testNewAccount("test_verify_initial_deposit"))
    suite.addTest(testNewAccount("test_verify_account_type_dropdown"))
    suite.addTest(testNewAccount("test_reset_button"))
    suite.addTest(testNewAccount("test_submit_button"))
    suite.addTest(testNewAccount("test_next_page"))
  

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
