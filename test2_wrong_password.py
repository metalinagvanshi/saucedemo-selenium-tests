# Test 2: Login with a wrong password
# Expected result: login should NOT happen, and an error message should show

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Open Chrome
driver = webdriver.Chrome()

# Step 2: Go to the demo shopping website
driver.get("https://www.saucedemo.com")
time.sleep(2)

# Step 3: Type correct username but WRONG password, then click Login
driver.find_element(By.ID, "user-name").send_keys("metali")
driver.find_element(By.ID, "password").send_keys("fghgdgfd")
time.sleep(1)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Step 4: Check the result
# Check 1: we should still be on the login page (login did NOT happen)
still_on_login_page = driver.current_url == "https://www.saucedemo.com/"

# Check 2: the red error message should be on the screen
error_text = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
error_shown = "do not match" in error_text

if still_on_login_page and error_shown:
    print("PASS: Login blocked, error shown ->", error_text)
else:
    print("FAIL: Something is wrong. URL:", driver.current_url, "| Error:", error_text)

# Step 5: Close Chrome
time.sleep(10)
driver.quit()
