from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

driver.get("http://localhost:8000")

try:
    input_box = driver.find_element(By.ID, "name")
    input_box.send_keys("Rubab")

    submit_btn = driver.find_element(By.ID, "submit")
    submit_btn.click()

    time.sleep(1)
    message = driver.find_element(By.ID, "message").text
    assert "Thank you" in message
    print("✅ Test Passed")
except Exception as e:
    print("❌ Test Failed:", e)
finally:
    driver.quit()
