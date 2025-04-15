import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys, ActionChains

class testEditCustomer(unittest.TestCase):
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
        driver.find_element(By.NAME, "emailid").send_keys("TestCustomer154@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("123")
        driver.find_element(By.NAME, "sub").click()


    def verify_customer_id(self):
        driver = self.driver
        # customer_id = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(4) td:nth-child(2)").text
        driver.find_element(By.LINK_TEXT, "Edit Customer").click()

        #EC1
        driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message14").text
        assert "Customer ID is required" in error_message, "Blank Customer ID Error Message Missing"

        #EC2
        driver.find_element(By.NAME, "cusid").send_keys("1234Acc")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Characters are not allowed" in error_message, "Customer ID Character Error Message Missing"

        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Characters are not allowed" in error_message, "Customer ID Character Error Message Missing"

        #EC3
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Special characters are not allowed" in error_message, "Customer ID Special Character Error Message Missing"

        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message14").text
        assert "Special characters are not allowed" in error_message, "Customer ID Special Character Error Message Missing"

        #EC4
        driver.find_element(By.NAME, "cusid").clear()
        driver.find_element(By.NAME, "cusid").send_keys("21303")
        driver.find_element(By.NAME, "AccSubmit").click()
        success_message = driver.find_element(By.CSS_SELECTOR,".heading3").text
        assert "Edit Customer" in success_message, "Error Not Directed To Edit Customer Page"

    def verify_address_field(self):
        driver = self.driver

        #EC5
        driver.find_element(By.NAME, "addr").clear()
        driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message3").text
        assert "Address Field must not be blank" in error_message, "Empty Address Error Message Missing"
    
    def verify_city_field(self):
        driver = self.driver

        #EC6
        driver.find_element(By.NAME, "city").clear()
        driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message4").text
        assert "City Field must not be blank" in error_message, "Empty City Error Message Missing"

        #EC7
        driver.find_element(By.NAME, "city").send_keys("1234")
        error_message = driver.find_element(By.ID, "message4").text
        assert "Numbers are not allowed" in error_message, "City Numeric Error Message Missing"
      
        driver.find_element(By.NAME, "city").send_keys("city123")
        error_message = driver.find_element(By.ID, "message4").text
        assert "Numbers are not allowed" in error_message, "City Numeric Error Message Missing"

        #EC8
        driver.find_element(By.NAME, "city").send_keys("City!@#")
        error_message = driver.find_element(By.ID, "message4").text
        assert "Special characters are not allowed" in error_message, "City Special Character Error Message Missing"

        driver.find_element(By.NAME, "city").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message4").text
        assert "Special characters are not allowed" in error_message, "City Special Character Error Message Missing"

    def verify_state_field(self):
        driver = self.driver

        #EC9
        driver.find_element(By.NAME, "state").clear()
        driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message5").text
        assert "State must not be blank" in error_message, "Empty State Error Message Missing"

        #EC10
        driver.find_element(By.NAME, "state").send_keys("1234")
        error_message = driver.find_element(By.ID, "message5").text
        assert "Numbers are not allowed" in error_message, "State Numeric Error Message Missing"

        driver.find_element(By.NAME, "state").clear()
        driver.find_element(By.NAME, "state").send_keys("state123")
        error_message = driver.find_element(By.ID, "message5").text
        assert "Numbers are not allowed" in error_message, "State Numeric Error Message Missing"

        #EC11
        driver.find_element(By.NAME, "state").clear()
        driver.find_element(By.NAME, "state").send_keys("State!@#")
        error_message = driver.find_element(By.ID, "message5").text
        assert "Special characters are not allowed" in error_message, "State Special Character Error Message Missing"

        driver.find_element(By.NAME, "state").clear()
        driver.find_element(By.NAME, "state").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message5").text
        assert "Special characters are not allowed" in error_message, "State Special Character Error Message Missing"

    def verify_pin_field(self):
        driver = self.driver

        #EC12
        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("123PIN")
        error_message = driver.find_element(By.ID, "message6").text
        assert "Characters are not allowed" in error_message, "Pin Character Error Message Missing"

        #EC13
        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message6").text
        assert "PIN Code must not be blank" in error_message, "Pin Blank Error Message Missing"

        #EC14
        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("123")
        error_message = driver.find_element(By.ID, "message6").text
        assert "PIN Code must have 6 Digits" in error_message, "Pin Amount Error Message Missing"

        #EC15
        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message6").text
        assert "Special characters are not allowed" in error_message, "Pin Special Character Error Message Missing"

    def verify_mobile_number_field(self):
        driver = self.driver
        #EC16
        driver.find_element(By.NAME, "telephoneno").clear()
        driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message7").text
        assert "Mobile no must not be blank" in error_message, "Phone Blank Error Message Missing"

        #EC17
        driver.find_element(By.NAME, "telephoneno").clear()
        driver.find_element(By.NAME, "telephoneno").send_keys("886636!@12")
        error_message = driver.find_element(By.ID, "message7").text
        assert "Special characters are not allowed" in error_message, "Phone Special Character Error Message Missing"

        driver.find_element(By.NAME, "telephoneno").clear()
        driver.find_element(By.NAME, "telephoneno").send_keys("!@88662682")
        error_message = driver.find_element(By.ID, "message7").text
        assert "Special characters are not allowed" in error_message, "Phone Special Character Error Message Missing"

        driver.find_element(By.NAME, "telephoneno").clear()
        driver.find_element(By.NAME, "telephoneno").send_keys("88663682!@")
        error_message = driver.find_element(By.ID, "message7").text
        assert "Special characters are not allowed" in error_message, "Phone Special Character Error Message Missing"

    def verify_email_field(self):
        driver = self.driver
        #EC18
        driver.find_element(By.NAME, "emailid").clear()
        driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID must not be blank" in error_message, "Email Blank Error Message Missing"

        #EC19
        driver.find_element(By.NAME, "emailid").clear()
        driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail")
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID is not valid" in error_message, "Email Invalid Error Message Missing"

        driver.find_element(By.NAME, "emailid").clear()
        driver.find_element(By.NAME, "emailid").send_keys("guru99")
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID is not valid" in error_message, "Email Invalid Error Message Missing"

        driver.find_element(By.NAME, "emailid").clear()
        driver.find_element(By.NAME, "emailid").send_keys("Guru99@")
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID is not valid" in error_message, "Email Invalid Error Message Missing"

        driver.find_element(By.NAME, "emailid").clear()
        driver.find_element(By.NAME, "emailid").send_keys("gurugmail.com")
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID is not valid" in error_message, "Email Invalid Error Message Missing"

    def submit_button(self):
        driver = self.driver
        #EC20 -- it opens blank page not sure how to assert it (the changes save)
        driver.find_element(By.NAME, "sub").click()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testEditCustomer("manager_login"))
    # suite.addTest(testEditCustomer("create_customer"))
    suite.addTest(testEditCustomer("verify_customer_id"))
    suite.addTest(testEditCustomer("verify_address_field"))
    suite.addTest(testEditCustomer("verify_city_field"))
    suite.addTest(testEditCustomer("verify_state_field"))
    suite.addTest(testEditCustomer("verify_pin_field"))
    suite.addTest(testEditCustomer("verify_mobile_number_field"))
    suite.addTest(testEditCustomer("verify_email_field"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)