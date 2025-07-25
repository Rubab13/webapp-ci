# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class WebAppTest(unittest.TestCase):
  
#     def setUp(self):
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")

#         self.driver = webdriver.Chrome(options=chrome_options)
#         self.driver.get("http://localhost:5500")
#           # self.driver = webdriver.Chrome()
#           # self.driver.get("http://localhost:5500")

#     # def setUp(self):
#     #     self.driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
#     #     self.driver.get("http://localhost:5500")  # Your local app URL

#     # def setUp(self):
#     #     options = webdriver.ChromeOptions()
#     #     options.add_argument('--headless')
#     #     options.add_argument('--no-sandbox')
#     #     options.add_argument('--disable-dev-shm-usage')

#     #     self.driver = webdriver.Chrome(options=options)
#     #     self.driver.get("http://localhost:8081")  # Change port as per your docker-compose


# # ----------------------------------------------------------------------------------------------------------------------------
#     # testing a web page title
#     # this function will search the title tag in the html of the page and if it is found as specified, this test case will be passed.
#     def test_title(self):
#         self.assertIn("User Book Collection", self.driver.title)
# # ----------------------------------------------------------------------------------------------------------------------------

# # ----------------------------------------------------------------------------------------------------------------------------
#     # test case to ensure that usr should not be able to click on the login button if he hasn't entered anything in the email and password fields
#     def test_signin_button_disabled_when_empty(self):
#       driver = self.driver
      
#       # Locate elements
#       email_input = driver.find_element(By.ID, "email")
#       password_input = driver.find_element(By.ID, "password")
#       signin_button = driver.find_element(By.ID, "signin-btn")   # -> for login button
      
#       # Make sure both fields are empty
#       self.assertEqual(email_input.get_attribute("value"), "")
#       self.assertEqual(password_input.get_attribute("value"), "")
      
#       # Check that the Sign In button is disabled
#       self.assertFalse(signin_button.is_enabled(), "Sign In button should be disabled when fields are empty")
# # ----------------------------------------------------------------------------------------------------------------------------

# # ----------------------------------------------------------------------------------------------------------------------------
#     # test case to ensure that usr should not be able to click on the sign up button if he hasn't entered anything in the email and password fields
#     def test_signup_button_disabled_when_empty(self):
#       driver = self.driver
      
#       # Locate elements
#       email_input = driver.find_element(By.ID, "email")
#       password_input = driver.find_element(By.ID, "password")
#       signin_button = driver.find_element(By.ID, "signup-btn")   # -> for sign up button
      
#       # Make sure both fields are empty
#       self.assertEqual(email_input.get_attribute("value"), "")
#       self.assertEqual(password_input.get_attribute("value"), "")
      
#       # Check that the Sign In button is disabled
#       self.assertFalse(signin_button.is_enabled(), "Sign Up button should be disabled when fields are empty")
# # ----------------------------------------------------------------------------------------------------------------------------

# # ----------------------------------------------------------------------------------------------------------------------------
#   # test case to ensure that if the password and confirm passwords fields are different the sign up button should be disabled and a warning message should be displayed.
#     def test_password_mismatch_disables_signup(self):
#       driver = self.driver

#       # Locate fields
#       email_input = driver.find_element(By.ID, "email")
#       password_input = driver.find_element(By.ID, "password")
#       confirm_password_input = driver.find_element(By.ID, "confirm-password")
#       signup_button = driver.find_element(By.ID, "signup-btn")
      
#       # Fill inputs
#       email_input.send_keys("test@example.com")
#       password_input.send_keys("12345678")
#       confirm_password_input.send_keys("wrongpass")

#       time.sleep(0.5)  # Allow JS to react
      
#       # Check: signup button is disabled
#       self.assertFalse(signup_button.is_enabled(), "Sign Up button should be disabled when passwords mismatch")

#       # Check: warning message is visible
#       warning = driver.find_element(By.ID, "password-warning")
#       self.assertTrue(warning.is_displayed(), "Password mismatch warning should be visible")
# # ----------------------------------------------------------------------------------------------------------------------------

# # ----------------------------------------------------------------------------------------------------------------------------
#   # Password match enables Sign Up button
#     def test_signup_button_enabled_when_passwords_match(self):
#       driver = self.driver

#       driver.find_element(By.ID, "email").send_keys("user@example.com")
#       driver.find_element(By.ID, "password").send_keys("12345678")
#       driver.find_element(By.ID, "confirm-password").send_keys("12345678")

#       time.sleep(0.5)
#       signup_btn = driver.find_element(By.ID, "signup-btn")

#       self.assertTrue(signup_btn.is_enabled(), "Sign Up button should be enabled when passwords match")

# # ----------------------------------------------------------------------------------------------------------------------------
  
# # ----------------------------------------------------------------------------------------------------------------------------
#   # Book section is hidden before login
#     def test_book_section_hidden_before_login(self):
#       book_section = self.driver.find_element(By.ID, "book-section")
#       self.assertFalse(book_section.is_displayed(), "Book section should be hidden before login")

# # ----------------------------------------------------------------------------------------------------------------------------
  
# # ----------------------------------------------------------------------------------------------------------------------------
#   # Add Book button is disabled if fields are empty
#     def test_add_book_disabled_when_fields_empty(self):
#       driver = self.driver

#       # Step 1: Log in
#       driver.find_element(By.ID, "email").send_keys("testuser@example.com")
#       driver.find_element(By.ID, "password").send_keys("12345678")
#       driver.find_element(By.ID, "signin-btn").click()

#       # Step 2: Wait for book section to be visible
#       WebDriverWait(driver, 10).until(
#           EC.visibility_of_element_located((By.ID, "book-section"))
#       )

#       # Step 3: Try submitting with empty fields
#       add_button = driver.find_element(By.CSS_SELECTOR, '#book-form button[type="submit"]')

#       title_input = driver.find_element(By.ID, "title")
#       author_input = driver.find_element(By.ID, "author")

#       # Clear just in case
#       title_input.clear()
#       author_input.clear()

#       # Optional: Check if form is invalid or button is disabled
#       self.assertEqual(title_input.get_attribute("value"), "")
#       self.assertEqual(author_input.get_attribute("value"), "")
      
#       # Try clicking it (shouldn't add anything)
#       add_button.click()

#       # Wait a moment and ensure no book was added (optional check)
#       book_list = driver.find_element(By.ID, "book-list")
#       self.assertEqual(book_list.text.strip(), "", "No book should be added if inputs are empty")

# # ----------------------------------------------------------------------------------------------------------------------------

# # ----------------------------------------------------------------------------------------------------------------------------
#   # Password must contain at least one digit
#     def test_password_requires_digit(self):
#         driver = self.driver

#         # Fill the form with a password that has no digits
#         driver.find_element(By.ID, "email").send_keys("nodigit@example.com")
#         driver.find_element(By.ID, "password").send_keys("NoDigitsHere")
#         driver.find_element(By.ID, "confirm-password").send_keys("NoDigitsHere")

#         time.sleep(0.5)

#         signup_btn = driver.find_element(By.ID, "signup-btn")
#         warning = driver.find_element(By.ID, "password-digit-warning")

#         # Button should remain disabled
#         # self.assertFalse(signup_btn.is_enabled(), "Sign Up button should be disabled if password has no digits")

#         # Warning message should be visible
#         self.assertTrue(warning.is_displayed(), "Digit warning should be shown for password without numbers")
# # ----------------------------------------------------------------------------------------------------------------------------

# # ----------------------------------------------------------------------------------------------------------------------------
#   #  Invalid Email Warning
#     def test_invalid_email_shows_warning(self):
#         driver = self.driver

#         # Input invalid email
#         driver.find_element(By.ID, "email").send_keys("invalid-email")
#         driver.find_element(By.ID, "password").send_keys("pass1234")
#         driver.find_element(By.ID, "confirm-password").send_keys("pass1234")

#         time.sleep(0.5)

#         signup_btn = driver.find_element(By.ID, "signup-btn")
#         email_warning = driver.find_element(By.ID, "email-warning")

#         # self.assertFalse(signup_btn.is_enabled(), "Sign Up button should be disabled for invalid email")
#         self.assertTrue(email_warning.is_displayed(), "Warning should appear for invalid email format")
# # ----------------------------------------------------------------------------------------------------------------------------

# # ----------------------------------------------------------------------------------------------------------------------------
#   # Reset button test
#     def test_reset_button_clears_fields(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:5500")  # Update path if needed

#         # Locate fields
#         email_input = driver.find_element(By.ID, "email")
#         password_input = driver.find_element(By.ID, "password")
#         confirm_password_input = driver.find_element(By.ID, "confirm-password")
#         reset_button = driver.find_element(By.ID, "reset-btn")

#         # Fill the fields
#         email_input.send_keys("test@example.com")
#         password_input.send_keys("Test1234")
#         confirm_password_input.send_keys("Test1234")

#         # Click the reset button
#         reset_button.click()
#         time.sleep(1)  # Wait for JS to execute

#         # Assert fields are empty
#         self.assertEqual(email_input.get_attribute("value"), "")
#         self.assertEqual(password_input.get_attribute("value"), "")
#         self.assertEqual(confirm_password_input.get_attribute("value"), "")
# # ----------------------------------------------------------------------------------------------------------------------------

#     def tearDown(self):
#       time.sleep(1)  # Just to see before closing browser
#       self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()


# above code before

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time

# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")

# driver = webdriver.Chrome(options=options)

# driver.get("http://13.60.235.48:8000")

# # test case 1
# def test_title():
#   assert "Book Collection" in driver.title

# test_title()

# driver.quit()

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class WebAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.binary_location = "/usr/bin/chromium-browser"  # in case needed
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("http://13.60.235.48:8000")
    
    # def setUp(self):
    #     """Clear input fields before each test."""
    #     driver = self.driver
    #     try:
    #         email = driver.find_element(By.ID, "email")
    #         password = driver.find_element(By.ID, "password")
    #         confirm = driver.find_element(By.ID, "confirm-password")

    #         email.clear()
    #         password.clear()
    #         confirm.clear()

    #         # Click reset if needed
    #         reset_btn = driver.find_element(By.ID, "reset-btn")
    #         driver.execute_script("arguments[0].click();", reset_btn)
    #         time.sleep(0.3)
    #     except Exception as e:
    #         print(f"Setup warning (not critical): {e}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # test case 1
    def test_01_title(self):
        """Page title should contain 'Book Collection'"""
        self.assertIn("Book Collection", self.driver.title)

    # test case 2
    def test_02_signin_button_disabled_when_empty(self):
        """Sign In button should be disabled when fields are empty"""
        driver = self.driver
        try:
            email_input = driver.find_element(By.ID, "email")
            password_input = driver.find_element(By.ID, "password")
            signin_button = driver.find_element(By.ID, "signin-btn")

            # Ensure fields are empty
            self.assertEqual(email_input.get_attribute("value"), "")
            self.assertEqual(password_input.get_attribute("value"), "")

            # Sign In button should be disabled
            self.assertFalse(signin_button.is_enabled(), "Sign In button should be disabled when fields are empty")
        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")
            
    # test case 3
    def test_03_signup_button_disabled_when_empty(self):
        """Sign Up button should be disabled when fields are empty"""
        driver = self.driver
        try:
            email_input = driver.find_element(By.ID, "email")
            password_input = driver.find_element(By.ID, "password")
            signup_button = driver.find_element(By.ID, "signup-btn")

            self.assertEqual(email_input.get_attribute("value"), "")
            self.assertEqual(password_input.get_attribute("value"), "")
            self.assertFalse(signup_button.is_enabled(), "Sign Up button should be disabled when fields are empty")
        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")
    
    # test case 4
    # Sign In Button is Enabled by Default
    def test_04_signin_button_is_disabled_by_default(self):
      """Sign In button should be enabled on page load"""
      signin_btn = self.driver.find_element(By.ID, "signin-btn")
      self.assertFalse(signin_btn.is_enabled(), "Sign In button should be disabled by default")
      
    # test case 5 
    # Sign Up Button is Disabled by Default
    def test_05_signup_button_is_disabled_by_default(self):
      """Sign Up button should be disabled on page load"""
      signup_btn = self.driver.find_element(By.ID, "signup-btn")
      self.assertFalse(signup_btn.is_enabled(), "Sign Up button should be disabled by default")
    
    # test case 6
    def test_06_invalid_email_shows_warning(self):
      driver = self.driver

      # Enter invalid email
      email_input = driver.find_element(By.ID, "email")
      email_input.clear()
      email_input.send_keys("invalid-email")  # No @ or domain

      # Trigger validation by focusing another field
      password_input = driver.find_element(By.ID, "password")
      password_input.click()

      time.sleep(0.5)  # Wait for JS validation

      warning = driver.find_element(By.ID, "email-warning")
      self.assertTrue(warning.is_displayed(), "Email warning should be shown for invalid email")

      # Clear fields to avoid affecting other tests
      email_input.clear()
      password_input.clear()
      if driver.find_element(By.ID, "confirm-password"):
          driver.find_element(By.ID, "confirm-password").clear()
    
    # test case 7
    def test_07_password_without_digit_shows_warning(self):
      driver = self.driver

      # Locate password input and warning element
      password_input = driver.find_element(By.ID, "password")
      warning = driver.find_element(By.ID, "password-digit-warning")

      # Clear and enter password without digit
      password_input.clear()
      password_input.send_keys("NoDigitsHere")

      # Trigger validation (click confirm password or blur)
      confirm_password_input = driver.find_element(By.ID, "confirm-password")
      confirm_password_input.click()

      time.sleep(0.5)  # Wait for JS validation

      # Assert that warning becomes visible
      self.assertTrue(warning.is_displayed(), "Password warning should be shown when there is no digit")

      # Clean up for next tests
      password_input.clear()
      confirm_password_input.clear()
    
    # test case 8
    def test_08_password_mismatch_shows_warning(self):
      driver = self.driver

      # Locate inputs
      password_input = driver.find_element(By.ID, "password")
      confirm_input = driver.find_element(By.ID, "confirm-password")
      warning = driver.find_element(By.ID, "password-warning")

      # Enter mismatching passwords
      password_input.clear()
      confirm_input.clear()
      password_input.send_keys("Test1234")
      confirm_input.send_keys("Mismatch123")

      time.sleep(0.5)  # Allow JS to process

      # Check that mismatch warning is visible
      self.assertTrue(warning.is_displayed(), "Password mismatch warning should be shown")

      # Clean inputs
      password_input.clear()
      confirm_input.clear()
  
    # test case 9
    def test_09_confirm_password_input_exists(self):
      """Confirm Password input should exist"""
      confirm_password_input = self.driver.find_element(By.ID, "confirm-password")
      self.assertEqual(confirm_password_input.get_attribute("type"), "password")
    
    # test case 10
    def test_10_book_section_hidden_initially(self):
      """Book section should be hidden on initial load"""
      book_section = self.driver.find_element(By.ID, "book-section")
      self.assertEqual(book_section.value_of_css_property("display"), "none")

if __name__ == "__main__":
    unittest.main()
