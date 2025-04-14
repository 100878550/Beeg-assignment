import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class testNewCustomer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://demo.guru99.com/V4/")
        
    @classmethod
    def teardown_method(cls):
        cls.driver.quit()
    

    def test_NC1_verify_name(self):
        driver = self.driver
        driver.find_element(By.NAME, "uid").send_keys("")
        driver.find_element(By.NAME, "password").send_keys("password123")
        driver.find_element(By.NAME, "btnLogin").click()
        
        # Wait for the page to load and the element to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "New Customer"))
        )
        
        driver.find_element(By.LINK_TEXT, "New Customer").click()
        
        # Verify the presence of the 'Customer Name' field
        assert driver.find_element(By.NAME, "name").is_displayed(), "Customer Name must not be blank"

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(testNewCustomer("test_NC1_verify_name"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
