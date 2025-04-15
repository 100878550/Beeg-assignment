import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.alert import Alert

class testDeleteCustomer(unittest.TestCase):
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
        driver.find_element(By.NAME, "emailid").send_keys("TestCustomer12@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("123")
        driver.find_element(By.NAME, "sub").click()
        time.sleep(5)
        global customer_id
        customer_id = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(4) td:nth-child(2)").text


    def verify_customer_id(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Delete Customer").click()

        #DC1
        driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message14").text
        assert "Customer ID is required" in error_message, "Blank Customer ID Error Message Missing"

        #DC2
        driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Characters are not allowed" in error_message, "Customer ID Character Error Message Missing" 

        #DC3
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Special characters are not allowed" in error_message, "Customer ID Special Character Error Message Missing"

        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Special characters are not allowed" in error_message, "Customer ID Special Character Error Message Missing"

        #DC4
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("123 12")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Characters are not allowed" in error_message, "Customer ID Blank Space Error Message Missing"

        #DC5
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys(" ")
        error_message = driver.find_element(By.ID, "message14").text
        assert "First character can not have space" in error_message, "Customer ID First Space Blank Error Message Missing"

    def submit_button(self):
        driver = self.driver
        #DC6
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("123456")
        driver.find_element(By.NAME, "AccSubmit").click()
        alert = driver.switch_to.alert
        alert.accept()
        alert = driver.switch_to.alert
        alertText = alert.text
        alert.accept()
        assert "Customer does not exist!!" in alertText, "Customer ID Does Not Exist Error Message Missing"

        #DC7 -- doesnt load website or message but does delete account
        time.sleep(2)
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys(customer_id)
        driver.find_element(By.NAME, "AccSubmit").click()
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(5)
        alert = driver.switch_to.alert
        alertText = alert.text
        alert.accept()
        assert "Customer does not existcould not be deleted!! First delete all accounts of this customer then delete the customer" in alertText, "Your Customer ID Message Missing"
    
    def reset_button(self):
        driver = self.driver
        #DC8
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("qwer")
        driver.find_element(By.NAME, "res").click()
        text_field = driver.find_element(By.NAME, "cusid").text

        assert "" in text_field, "Text Not Reset"

     
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("123456")
        driver.find_element(By.NAME, "res").click()
        text_field = driver.find_element(By.NAME, "cusid").text

        assert "" in text_field, "Text Not Reset"

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testDeleteCustomer("manager_login"))
    suite.addTest(testDeleteCustomer("create_customer"))
    suite.addTest(testDeleteCustomer("verify_customer_id"))
    suite.addTest(testDeleteCustomer("submit_button"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)