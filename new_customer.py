import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys, ActionChains

class testNewCustomer(unittest.TestCase):
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


    def verify_name_field(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "New Customer").click()

        #NC1
        driver.find_element(By.NAME, "name").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message").text
        assert "Customer name must not be blank" in error_message, "Blank Customer Name Error Message Missing"

        #NC2
        driver.find_element(By.NAME, "name").send_keys("name123")
        error_message = driver.find_element(By.ID, "message").text
        assert "Numbers are not allowed" in error_message, "Numeric Customer Name Error Message Missing"

        driver.find_element(By.NAME, "name").clear()
        driver.find_element(By.NAME, "name").send_keys("1234")
        error_message = driver.find_element(By.ID, "message").text
        assert "Numbers are not allowed" in error_message, "Numeric Customer Name Error Message Missing"

        #NC3
        driver.find_element(By.NAME, "name").clear()
        driver.find_element(By.NAME, "name").send_keys("name!@#")
        error_message = driver.find_element(By.ID, "message").text
        assert "Special characters are not allowed" in error_message, "Special Character Customer Name Error Message Missing"

        driver.find_element(By.NAME, "name").clear()
        driver.find_element(By.NAME, "name").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message").text
        assert "Special characters are not allowed" in error_message, "Special Character Customer Name Error Message Missing"

        #NC4
        driver.find_element(By.NAME, "name").clear()
        driver.find_element(By.NAME, "name").send_keys(" ")
        error_message = driver.find_element(By.ID, "message").text
        assert "First character can not have space" in error_message, "First Space Blank Customer Name Error Message Missing"

    def verify_address_field(self):
        driver = self.driver
        #NC5
        driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message3").text
        assert "Address Field must not be blank" in error_message, "Blank Address Error Message Missing"

        #NC6
        driver.find_element(By.NAME, "addr").send_keys(" ")
        error_message = driver.find_element(By.ID, "message3").text
        assert "First character can not have space" in error_message, "First Space Blank Address Error Message Missing"

    def verify_city_field(self):
        driver = self.driver
        #NC7
        driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message4").text
        assert "City Field must not be blank" in error_message, "Blank City Error Message Missing"

        #NC8
        driver.find_element(By.NAME, "city").send_keys("city123")
        error_message = driver.find_element(By.ID, "message4").text
        assert "Numbers are not allowed" in error_message, "Numeric City Error Message Missing"

        driver.find_element(By.NAME, "city").clear()
        driver.find_element(By.NAME, "city").send_keys("1234")
        error_message = driver.find_element(By.ID, "message4").text
        assert "Numbers are not allowed" in error_message, "Numeric City Error Message Missing"

        #NC9
        driver.find_element(By.NAME, "city").clear()
        driver.find_element(By.NAME, "city").send_keys("city!@#")
        error_message = driver.find_element(By.ID, "message4").text
        assert "Special characters are not allowed" in error_message, "Special Character City Error Message Missing"

        driver.find_element(By.NAME, "city").clear()
        driver.find_element(By.NAME, "city").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message4").text
        assert "Special characters are not allowed" in error_message, "Special Character City Error Message Missing"

        #NC10
        driver.find_element(By.NAME, "city").clear()
        driver.find_element(By.NAME, "city").send_keys(" ")
        error_message = driver.find_element(By.ID, "message4").text
        assert "First character can not have space" in error_message, "First Space Blank City Error Message Missing"

    def verify_state_field(self):
        driver = self.driver
        #NC11
        driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message5").text
        assert "State must not be blank" in error_message, "Blank State Error Message Missing"

        #NC12
        driver.find_element(By.NAME, "state").send_keys("state123")
        error_message = driver.find_element(By.ID, "message5").text
        assert "Numbers are not allowed" in error_message, "Numeric State Error Message Missing"

        driver.find_element(By.NAME, "state").clear()
        driver.find_element(By.NAME, "state").send_keys("1234")
        error_message = driver.find_element(By.ID, "message5").text
        assert "Numbers are not allowed" in error_message, "Numeric State Error Message Missing"

        #NC13
        driver.find_element(By.NAME, "state").clear()
        driver.find_element(By.NAME, "state").send_keys("state!@#")
        error_message = driver.find_element(By.ID, "message5").text
        assert "Special characters are not allowed" in error_message, "Special Character State Error Message Missing"

        driver.find_element(By.NAME, "state").clear()
        driver.find_element(By.NAME, "state").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message5").text
        assert "Special characters are not allowed" in error_message, "Special Character State Error Message Missing"

        #NC14
        driver.find_element(By.NAME, "state").clear()
        driver.find_element(By.NAME, "state").send_keys(" ")
        error_message = driver.find_element(By.ID, "message5").text
        assert "First character can not have space" in error_message, "First Space Blank State Error Message Missing" 
    
    def verify_pin_field(self):
        driver = self.driver
        #NC15
        driver.find_element(By.NAME, "pinno").send_keys("1234PIN")
        error_message = driver.find_element(By.ID, "message6").text
        assert "Characters are not allowed" in error_message, "Pin Character Error Message Missing"

        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("PIN")
        error_message = driver.find_element(By.ID, "message6").text
        assert "Characters are not allowed" in error_message, "Pin Character Error Message Missing"

        #NC16
        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message6").text
        assert "PIN Code must not be blank" in error_message, "Blank Pin Error Message Missing"

        #NC17
        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("123")
        error_message = driver.find_element(By.ID, "message6").text
        assert "PIN Code must have 6 Digits" in error_message, "Pin Length Error Message Missing"


        #NC18
        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message6").text
        assert "Special characters are not allowed" in error_message, "Special Character Pin Error Message Missing" 

        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message6").text
        assert "Special characters are not allowed" in error_message, "Special Character Pin Error Message Missing" 

        #NC19
        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys(" ")
        error_message = driver.find_element(By.ID, "message6").text
        assert "First character can not have space" in error_message, "First Space Blank Pin Error Message Missing" 

        #NC20
        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("1 2 3")
        error_message = driver.find_element(By.ID, "message6").text
        assert "Characters are not allowed" in error_message, "Blank Space Pin Error Message Missing" 

    def verify_mobile_number_field(self):
        driver = self.driver
        #NC21
        driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message7").text
        assert "Mobile no must not be blank" in error_message, "Blank Phone Number Error Message Missing" 

        #NC22
        driver.find_element(By.NAME, "telephoneno").send_keys(" ")
        error_message = driver.find_element(By.ID, "message7").text
        assert "First character can not have space" in error_message, "First Space Blank Phone Number Error Message Missing" 

        #NC23
        driver.find_element(By.NAME, "telephoneno").clear()
        driver.find_element(By.NAME, "telephoneno").send_keys("1 2 3")
        error_message = driver.find_element(By.ID, "message7").text
        assert "Characters are not allowed" in error_message, "Blank Space Phone Number Error Message Missing" 

        #NC24
        driver.find_element(By.NAME, "telephoneno").clear()
        driver.find_element(By.NAME, "telephoneno").send_keys("886636!@12")
        error_message = driver.find_element(By.ID, "message7").text
        assert "Special characters are not allowed" in error_message, "Special Character Pin Error Message Missing" 

        driver.find_element(By.NAME, "telephoneno").clear()
        driver.find_element(By.NAME, "telephoneno").send_keys("!@88662682")
        error_message = driver.find_element(By.ID, "message7").text
        assert "Special characters are not allowed" in error_message, "Special Character Pin Error Message Missing" 

        driver.find_element(By.NAME, "telephoneno").clear()
        driver.find_element(By.NAME, "telephoneno").send_keys("88663682!@")
        error_message = driver.find_element(By.ID, "message7").text
        assert "Special characters are not allowed" in error_message, "Special Character Pin Error Message Missing" 

    def verify_email_field(self):
        driver = self.driver
        #NC25
        driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID must not be blank" in error_message, "Blank Email Error Message Missing" 

        #NC26
        driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail")
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID is not valid" in error_message, "Invalid Email Error Message Missing" 

        driver.find_element(By.NAME, "emailid").clear()
        driver.find_element(By.NAME, "emailid").send_keys("guru99")
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID is not valid" in error_message, "Invalid Email Error Message Missing" 

        driver.find_element(By.NAME, "emailid").clear()
        driver.find_element(By.NAME, "emailid").send_keys("Guru99@")
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID is not valid" in error_message, "Invalid Email Error Message Missing" 

        driver.find_element(By.NAME, "emailid").clear()
        driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail.")
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID is not valid" in error_message, "Invalid Email Error Message Missing" 

        driver.find_element(By.NAME, "emailid").clear()
        driver.find_element(By.NAME, "emailid").send_keys("guru99gmail.com")
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID is not valid" in error_message, "Invalid Email Error Message Missing" 

        #NC27 -- website error message missing
        driver.find_element(By.NAME, "emailid").clear()
        driver.find_element(By.NAME, "emailid").send_keys("gu ru 99@gmail.com")
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID is not valid" in error_message, "Blank Space Email Error Message Missing" 
    
    def verify_password_field(self):
        driver = self.driver
        #NC28
        driver.find_element(By.NAME, "password").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message18").text
        assert "Password must not be blank" in error_message, "Blank Password Error Message Missing" 

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testNewCustomer("manager_login"))
    suite.addTest(testNewCustomer("verify_name_field"))
    suite.addTest(testNewCustomer("verify_address_field"))
    suite.addTest(testNewCustomer("verify_city_field"))
    suite.addTest(testNewCustomer("verify_state_field"))
    suite.addTest(testNewCustomer("verify_pin_field"))
    suite.addTest(testNewCustomer("verify_mobile_number_field"))
    suite.addTest(testNewCustomer("verify_email_field"))
    suite.addTest(testNewCustomer("verify_password_field"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
