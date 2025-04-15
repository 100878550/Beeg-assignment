import new_customer
import edit_customer
import delete_customer
import new_account
import edit_account
import delete_account
import balance_enquiry
import mini_statement
import customised_statement
import unittest

while True:
    print("Menu")
    print("1. New Customer")
    print("2. Edit Customer")
    print("3. Delete Customer")
    print("4. New Account")
    print("5. Edit Account")
    print("6. Delete Account")
    print("7. Balance Enquiry")
    print("8. Mini Statement")
    print("9. Customised Statement")

    user_input = input("Please enter your choice: ")

    if user_input == '1':
        suite = unittest.TestLoader().loadTestsFromTestCase(new_customer.testNewCustomer)  # this just loads all the methods with test_ infront
        runner = unittest.TextTestRunner(verbosity=2).run(suite) # abd runs them

    elif user_input == '2':
        suite = unittest.TestLoader().loadTestsFromTestCase(edit_customer.testEditCustomer)
        runner = unittest.TextTestRunner(verbosity=2).run(suite)
        
    elif user_input == '3':
        suite = unittest.TestLoader().loadTestsFromTestCase(delete_customer.testDeleteCustomer)
        runner = unittest.TextTestRunner(verbosity=2).run(suite)
        
    elif user_input == '4':
        suite = unittest.TestLoader().loadTestsFromTestCase(new_account.testNewAccount)
        runner = unittest.TextTestRunner(verbosity=2).run(suite)
        
    elif user_input == '5':
        suite = unittest.TestLoader().loadTestsFromTestCase(edit_account.testEditAccount)
        runner = unittest.TextTestRunner(verbosity=2).run(suite)
        
    elif user_input == '6':
        suite = unittest.TestLoader().loadTestsFromTestCase(delete_account.testDeleteAccount)
        runner = unittest.TextTestRunner(verbosity=2).run(suite)
        
    elif user_input == '7':
        suite = unittest.TestLoader().loadTestsFromTestCase(balance_enquiry.testBalanceEnquiry)
        runner = unittest.TextTestRunner(verbosity=2).run(suite)
        
    elif user_input == '8':
        suite = unittest.TestLoader().loadTestsFromTestCase(mini_statement.testMiniStatement)
        runner = unittest.TextTestRunner(verbosity=2).run(suite)
        
    elif user_input == '9':
        suite = unittest.TestLoader().loadTestsFromTestCase(customised_statement.testCustomisedStatement)
        runner = unittest.TextTestRunner(verbosity=2).run(suite)

    else:
        print("Invalid choice! Please try again.")
