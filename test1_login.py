# Test 1: Login with correct username and password
# Expected result: the "Products" page should open

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Open Chrome
driver = webdriver.Chrome()

# Step 2: Go to the demo shopping website
driver.get("https://www.saucedemo.com")
time.sleep(2)  # wait 2 seconds so we can see it

# Step 3: Type username and password, then click Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Step 4: Check the result (this is the actual "test")
title = driver.find_element(By.CLASS_NAME, "title").text
if title == "Products":
    print("PASS: Login worked, Products page opened")
else:
    print("FAIL: Expected 'Products' but got:", title)

# Step 5: Close Chrome
time.sleep(2)
driver.quit()
