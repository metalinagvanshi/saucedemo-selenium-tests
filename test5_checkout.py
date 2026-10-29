# Test 5: Buy one item (full checkout)
# Expected result: the "Thank you for your order!" page should open

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Open Chrome
driver = webdriver.Chrome()

# Step 2: Go to the demo shopping website
driver.get("https://www.saucedemo.com")
time.sleep(2)

# Step 3: Login with correct username and password
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Step 4: Add the Backpack to the cart and open the cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

# Step 5: Click Checkout and fill in name and postal code
driver.find_element(By.ID, "checkout").click()
time.sleep(1)
driver.find_element(By.ID, "first-name").send_keys("Metali")
driver.find_element(By.ID, "last-name").send_keys("Nagvanshi")
driver.find_element(By.ID, "postal-code").send_keys("560001")
driver.find_element(By.ID, "continue").click()
time.sleep(2)

# Step 6: On the overview page, click Finish
driver.find_element(By.ID, "finish").click()
time.sleep(2)

# Step 7: Check the result
header = driver.find_element(By.CLASS_NAME, "complete-header").text
if header == "Thank you for your order!":
    print("PASS: Order placed ->", header)
else:
    print("FAIL: Expected 'Thank you for your order!' but got:", header)

# Step 8: Close Chrome
time.sleep(2)
driver.quit()
