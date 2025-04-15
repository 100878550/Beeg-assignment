import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains

class testNewCustomer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://demo.guru99.com")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def test_manager_login(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/")
        
        # Wait for the username field to be visible and enter the credentials
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "uid"))).send_keys("mngr618426")
        driver.find_element(By.NAME, "password").send_keys("mebedAz")
        
        # Wait for the login button to be clickable and click it
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnLogin")))
        login_button.click()

    def test_verify_name_field(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "New Customer").click()

        # NA1: Test empty name field
        driver.find_element(By.NAME, "name").send_keys(Keys.TAB)
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "message"))).text
        assert "Customer name must not be blank" in error_message, f"Expected 'Customer name must not be blank' but got {error_message}"

        # NA2: Test name with numbers
        driver.find_element(By.NAME, "name").clear()
        driver.find_element(By.NAME, "name").send_keys("name123")
        error_message = driver.find_element(By.ID, "message").text
        assert "Numbers are not allowed" in error_message, f"Expected 'Numbers are not allowed' but got {error_message}"

        # NA3: Test name with special characters
        driver.find_element(By.NAME, "name").clear()
        driver.find_element(By.NAME, "name").send_keys("name!@#")
        error_message = driver.find_element(By.ID, "message").text
        assert "Special characters are not allowed" in error_message, f"Expected 'Special characters are not allowed' but got {error_message}"

        # NA4: Test name with space
        driver.find_element(By.NAME, "name").clear()
        driver.find_element(By.NAME, "name").send_keys(" ")
        error_message = driver.find_element(By.ID, "message").text
        assert "First character can not have space" in error_message, f"Expected 'First character can not have space' but got {error_message}"

    def test_verify_address_field(self):
        driver = self.driver
        # NA5: Test empty address
        driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "message3"))).text
        assert "Address Field must not be blank" in error_message, f"Expected 'Address Field must not be blank' but got {error_message}"

        # NA6: Test address with leading space
        driver.find_element(By.NAME, "addr").send_keys(" ")
        error_message = driver.find_element(By.ID, "message3").text
        assert "First character can not have space" in error_message, f"Expected 'First character can not have space' but got {error_message}"

    def test_verify_city_field(self):
        driver = self.driver
        # NA7: Test empty city
        driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "message4"))).text
        assert "City Field must not be blank" in error_message, f"Expected 'City Field must not be blank' but got {error_message}"

        # NA8: Test city with numbers
        driver.find_element(By.NAME, "city").clear()
        driver.find_element(By.NAME, "city").send_keys("city123")
        error_message = driver.find_element(By.ID, "message4").text
        assert "Numbers are not allowed" in error_message, f"Expected 'Numbers are not allowed' but got {error_message}"

        # NA9: Test city with special characters
        driver.find_element(By.NAME, "city").clear()
        driver.find_element(By.NAME, "city").send_keys("city!@#")
        error_message = driver.find_element(By.ID, "message4").text
        assert "Special characters are not allowed" in error_message, f"Expected 'Special characters are not allowed' but got {error_message}"

        # NA10: Test city with space
        driver.find_element(By.NAME, "city").clear()
        driver.find_element(By.NAME, "city").send_keys(" ")
        error_message = driver.find_element(By.ID, "message4").text
        assert "First character can not have space" in error_message, f"Expected 'First character can not have space' but got {error_message}"

    def test_verify_state_field(self):
        driver = self.driver
        # NA11: Test empty state
        driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "message5"))).text
        assert "State must not be blank" in error_message, f"Expected 'State must not be blank' but got {error_message}"

        # NA12: Test state with numbers
        driver.find_element(By.NAME, "state").clear()
        driver.find_element(By.NAME, "state").send_keys("state123")
        error_message = driver.find_element(By.ID, "message5").text
        assert "Numbers are not allowed" in error_message, f"Expected 'Numbers are not allowed' but got {error_message}"

        # NA13: Test state with special characters
        driver.find_element(By.NAME, "state").clear()
        driver.find_element(By.NAME, "state").send_keys("state!@#")
        error_message = driver.find_element(By.ID, "message5").text
        assert "Special characters are not allowed" in error_message, f"Expected 'Special characters are not allowed' but got {error_message}"

        # NA14: Test state with space
        driver.find_element(By.NAME, "state").clear()
        driver.find_element(By.NAME, "state").send_keys(" ")
        error_message = driver.find_element(By.ID, "message5").text
        assert "First character can not have space" in error_message, f"Expected 'First character can not have space' but got {error_message}"

    def test_verify_pin_field(self):
        driver = self.driver
        # NA15–NA20
        driver.find_element(By.NAME, "pinno").send_keys("1234PIN")
        error_message = driver.find_element(By.ID, "message6").text
        assert "Characters are not allowed" in error_message, f"Expected 'Characters are not allowed' but got {error_message}"

        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("PIN")
        error_message = driver.find_element(By.ID, "message6").text
        assert "Characters are not allowed" in error_message, f"Expected 'Characters are not allowed' but got {error_message}"

        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        error_message = driver.find_element(By.ID, "message6").text
        assert "PIN Code must not be blank" in error_message, f"Expected 'PIN Code must not be blank' but got {error_message}"

        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("123")
        error_message = driver.find_element(By.ID, "message6").text
        assert "PIN Code must have 6 Digits" in error_message, f"Expected 'PIN Code must have 6 Digits' but got {error_message}"

        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("!@#")
        error_message = driver.find_element(By.ID, "message6").text
        assert "Special characters are not allowed" in error_message, f"Expected 'Special characters are not allowed' but got {error_message}"

        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("123!@#")
        error_message = driver.find_element(By.ID, "message6").text
        assert "Special characters are not allowed" in error_message, f"Expected 'Special characters are not allowed' but got {error_message}"

        driver.find_element(By.NAME, "pinno").clear()
        driver.find_element(By.NAME, "pinno").send_keys("1 2 3")
        error_message = driver.find_element(By.ID, "message6").text
        assert "Characters are not allowed" in error_message, f"Expected 'Characters are not allowed' but got {error_message}"

    def test_verify_mobile_number_field(self):
        driver = self.driver
        # NA21: Mobile field blank
        driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "message7"))).text
        assert "Mobile no must not be blank" in error_message, f"Expected 'Mobile no must not be blank' but got {error_message}"

        # NA22: Mobile with space
        driver.find_element(By.NAME, "telephoneno").clear()
        driver.find_element(By.NAME, "telephoneno").send_keys("1 2 3")
        error_message = driver.find_element(By.ID, "message7").text
        assert "Characters are not allowed" in error_message, f"Expected 'Characters are not allowed' but got {error_message}"

        # NA23: Mobile with special characters
        driver.find_element(By.NAME, "telephoneno").clear()
        driver.find_element(By.NAME, "telephoneno").send_keys("886636!@12")
        error_message = driver.find_element(By.ID, "message7").text
        assert "Special characters are not allowed" in error_message, f"Expected 'Special characters are not allowed' but got {error_message}"

    def test_verify_email_field(self):
        driver = self.driver
        # NA24: Email blank
        driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "message9"))).text
        assert "Email-ID must not be blank" in error_message, f"Expected 'Email-ID must not be blank' but got {error_message}"

        # NA25: Invalid email
        driver.find_element(By.NAME, "emailid").clear()
        driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail")
        error_message = driver.find_element(By.ID, "message9").text
        assert "Email-ID is not valid" in error_message, f"Expected 'Email-ID is not valid' but got {error_message}"

    def test_verify_password_field(self):
        driver = self.driver
        # NA26: Password blank
        driver.find_element(By.NAME, "password").send_keys(Keys.TAB)
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "message18"))).text
        assert "Password must not be blank" in error_message, f"Expected 'Password must not be blank' but got {error_message}"

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testNewCustomer("test_manager_login"))
    suite.addTest(testNewCustomer("test_verify_name_field"))
    suite.addTest(testNewCustomer("test_verify_address_field"))
    suite.addTest(testNewCustomer("test_verify_city_field"))
    suite.addTest(testNewCustomer("test_verify_state_field"))
    suite.addTest(testNewCustomer("test_verify_pin_field"))
    suite.addTest(testNewCustomer("test_verify_mobile_number_field"))
    suite.addTest(testNewCustomer("test_verify_email_field"))
    suite.addTest(testNewCustomer("test_verify_password_field"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


