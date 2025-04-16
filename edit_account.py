import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys, ActionChains

class testEditAccount(unittest.TestCase):
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
        # driver.find_element(By.NAME, "emailid").send_keys("ManagerTest@gmail.com")
        # driver.find_element(By.NAME, "btnLogin").click()
        # user_id = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(4) td:nth-child(2)").text
        # password = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(5) td:nth-child(2)").text
        driver.get("https://demo.guru99.com/V4/")
        driver.find_element(By.NAME, "uid").send_keys("mngr618426")
        driver.find_element(By.NAME, "password").send_keys("mebedAz")
        driver.find_element(By.NAME, "btnLogin").click()
    
    def test_verify_account_number(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Edit Account").click()

        #EA1
        driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message2").text
        assert "Account Number must not be blank" in error_message, "Acount Number Blank Error Message Missing"

        #EA2
        driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Characters are not allowed" in error_message, "Acount Number Character Error Message Missing"

        #EA3
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Special characters are not allowed" in error_message, "Acount Number Special Character Error Message Missing"

        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Special characters are not allowed" in error_message, "Acount Number Special Character Error Message Missing"

        #EA4
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123 12")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Characters are not allowed" in error_message, "Acount Number Blank Space Error Message Missing"

        #EA5
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys(" ")
        error_message = driver.find_element(By.ID, "message2").text
        assert "Characters are not allowed" in error_message, "Acount Number First Space Blank Error Message Missing"

    def test_verify_submit_button(self):
        driver = self.driver
        
        
        #EA7 
        time.sleep(3)
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("12345")
        driver.find_element(By.NAME, "AccSubmit").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alertText = alert.text
        alert.accept()
        assert "Account does not exist" in alertText, "InValid Acount Number Error Message Missing"

        #EA6 -- server error
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("144230")
        driver.find_element(By.NAME, "AccSubmit").click()

    def test_verify_reset_button(self):
        driver = self.driver
        #EA8
        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("qwer")
        driver.find_element(By.NAME, "res").click()
        text = driver.find_element(By.NAME, "accountno").text
        assert "" in text,"Reset Button Not Working"

        driver.find_element(By.NAME, "accountno").clear()
        driver.find_element(By.NAME, "accountno").send_keys("123456")
        driver.find_element(By.NAME, "res").click()
        text = driver.find_element(By.NAME, "accountno").text
        assert "" in text,"Reset Button Not Working"

    

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testEditAccount("test_manager_login"))
    suite.addTest(testEditAccount("test_verify_account_number"))
    suite.addTest(testEditAccount("test_verify_reset_button"))
    suite.addTest(testEditAccount("test_verify_submit_button"))
    


    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite) 