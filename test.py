import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebAppTest(unittest.TestCase):
  
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost:5500")
          # self.driver = webdriver.Chrome()
          # self.driver.get("http://localhost:5500")

    # def setUp(self):
    #     self.driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
    #     self.driver.get("http://localhost:5500")  # Your local app URL

    # def setUp(self):
    #     options = webdriver.ChromeOptions()
    #     options.add_argument('--headless')
    #     options.add_argument('--no-sandbox')
    #     options.add_argument('--disable-dev-shm-usage')

    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.get("http://localhost:8081")  # Change port as per your docker-compose


# ----------------------------------------------------------------------------------------------------------------------------
    # testing a web page title
    # this function will search the title tag in the html of the page and if it is found as specified, this test case will be passed.
    def test_title(self):
        self.assertIn("User Book Collection", self.driver.title)
# ----------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------
    # test case to ensure that usr should not be able to click on the login button if he hasn't entered anything in the email and password fields
    def test_signin_button_disabled_when_empty(self):
      driver = self.driver
      
      # Locate elements
      email_input = driver.find_element(By.ID, "email")
      password_input = driver.find_element(By.ID, "password")
      signin_button = driver.find_element(By.ID, "signin-btn")   # -> for login button
      
      # Make sure both fields are empty
      self.assertEqual(email_input.get_attribute("value"), "")
      self.assertEqual(password_input.get_attribute("value"), "")
      
      # Check that the Sign In button is disabled
      self.assertFalse(signin_button.is_enabled(), "Sign In button should be disabled when fields are empty")
# ----------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------
    # test case to ensure that usr should not be able to click on the sign up button if he hasn't entered anything in the email and password fields
    def test_signup_button_disabled_when_empty(self):
      driver = self.driver
      
      # Locate elements
      email_input = driver.find_element(By.ID, "email")
      password_input = driver.find_element(By.ID, "password")
      signin_button = driver.find_element(By.ID, "signup-btn")   # -> for sign up button
      
      # Make sure both fields are empty
      self.assertEqual(email_input.get_attribute("value"), "")
      self.assertEqual(password_input.get_attribute("value"), "")
      
      # Check that the Sign In button is disabled
      self.assertFalse(signin_button.is_enabled(), "Sign Up button should be disabled when fields are empty")
# ----------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------
  # test case to ensure that if the password and confirm passwords fields are different the sign up button should be disabled and a warning message should be displayed.
    def test_password_mismatch_disables_signup(self):
      driver = self.driver

      # Locate fields
      email_input = driver.find_element(By.ID, "email")
      password_input = driver.find_element(By.ID, "password")
      confirm_password_input = driver.find_element(By.ID, "confirm-password")
      signup_button = driver.find_element(By.ID, "signup-btn")
      
      # Fill inputs
      email_input.send_keys("test@example.com")
      password_input.send_keys("12345678")
      confirm_password_input.send_keys("wrongpass")

      time.sleep(0.5)  # Allow JS to react
      
      # Check: signup button is disabled
      self.assertFalse(signup_button.is_enabled(), "Sign Up button should be disabled when passwords mismatch")

      # Check: warning message is visible
      warning = driver.find_element(By.ID, "password-warning")
      self.assertTrue(warning.is_displayed(), "Password mismatch warning should be visible")
# ----------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------
  # Password match enables Sign Up button
    def test_signup_button_enabled_when_passwords_match(self):
      driver = self.driver

      driver.find_element(By.ID, "email").send_keys("user@example.com")
      driver.find_element(By.ID, "password").send_keys("12345678")
      driver.find_element(By.ID, "confirm-password").send_keys("12345678")

      time.sleep(0.5)
      signup_btn = driver.find_element(By.ID, "signup-btn")

      self.assertTrue(signup_btn.is_enabled(), "Sign Up button should be enabled when passwords match")

# ----------------------------------------------------------------------------------------------------------------------------
  
# ----------------------------------------------------------------------------------------------------------------------------
  # Book section is hidden before login
    def test_book_section_hidden_before_login(self):
      book_section = self.driver.find_element(By.ID, "book-section")
      self.assertFalse(book_section.is_displayed(), "Book section should be hidden before login")

# ----------------------------------------------------------------------------------------------------------------------------
  
# ----------------------------------------------------------------------------------------------------------------------------
  # Add Book button is disabled if fields are empty
    def test_add_book_disabled_when_fields_empty(self):
      driver = self.driver

      # Step 1: Log in
      driver.find_element(By.ID, "email").send_keys("testuser@example.com")
      driver.find_element(By.ID, "password").send_keys("12345678")
      driver.find_element(By.ID, "signin-btn").click()

      # Step 2: Wait for book section to be visible
      WebDriverWait(driver, 10).until(
          EC.visibility_of_element_located((By.ID, "book-section"))
      )

      # Step 3: Try submitting with empty fields
      add_button = driver.find_element(By.CSS_SELECTOR, '#book-form button[type="submit"]')

      title_input = driver.find_element(By.ID, "title")
      author_input = driver.find_element(By.ID, "author")

      # Clear just in case
      title_input.clear()
      author_input.clear()

      # Optional: Check if form is invalid or button is disabled
      self.assertEqual(title_input.get_attribute("value"), "")
      self.assertEqual(author_input.get_attribute("value"), "")
      
      # Try clicking it (shouldn't add anything)
      add_button.click()

      # Wait a moment and ensure no book was added (optional check)
      book_list = driver.find_element(By.ID, "book-list")
      self.assertEqual(book_list.text.strip(), "", "No book should be added if inputs are empty")

# ----------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------
  # Password must contain at least one digit
    def test_password_requires_digit(self):
        driver = self.driver

        # Fill the form with a password that has no digits
        driver.find_element(By.ID, "email").send_keys("nodigit@example.com")
        driver.find_element(By.ID, "password").send_keys("NoDigitsHere")
        driver.find_element(By.ID, "confirm-password").send_keys("NoDigitsHere")

        time.sleep(0.5)

        signup_btn = driver.find_element(By.ID, "signup-btn")
        warning = driver.find_element(By.ID, "password-digit-warning")

        # Button should remain disabled
        # self.assertFalse(signup_btn.is_enabled(), "Sign Up button should be disabled if password has no digits")

        # Warning message should be visible
        self.assertTrue(warning.is_displayed(), "Digit warning should be shown for password without numbers")
# ----------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------
  #  Invalid Email Warning
    def test_invalid_email_shows_warning(self):
        driver = self.driver

        # Input invalid email
        driver.find_element(By.ID, "email").send_keys("invalid-email")
        driver.find_element(By.ID, "password").send_keys("pass1234")
        driver.find_element(By.ID, "confirm-password").send_keys("pass1234")

        time.sleep(0.5)

        signup_btn = driver.find_element(By.ID, "signup-btn")
        email_warning = driver.find_element(By.ID, "email-warning")

        # self.assertFalse(signup_btn.is_enabled(), "Sign Up button should be disabled for invalid email")
        self.assertTrue(email_warning.is_displayed(), "Warning should appear for invalid email format")
# ----------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------
  # Reset button test
    def test_reset_button_clears_fields(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5500")  # Update path if needed

        # Locate fields
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")
        confirm_password_input = driver.find_element(By.ID, "confirm-password")
        reset_button = driver.find_element(By.ID, "reset-btn")

        # Fill the fields
        email_input.send_keys("test@example.com")
        password_input.send_keys("Test1234")
        confirm_password_input.send_keys("Test1234")

        # Click the reset button
        reset_button.click()
        time.sleep(1)  # Wait for JS to execute

        # Assert fields are empty
        self.assertEqual(email_input.get_attribute("value"), "")
        self.assertEqual(password_input.get_attribute("value"), "")
        self.assertEqual(confirm_password_input.get_attribute("value"), "")
# ----------------------------------------------------------------------------------------------------------------------------

    def tearDown(self):
      time.sleep(1)  # Just to see before closing browser
      self.driver.quit()

if __name__ == "__main__":
    unittest.main()
