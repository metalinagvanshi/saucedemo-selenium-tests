# Test 4: Remove an item from the cart
# Expected result: cart icon number goes away, and the button changes back to "Add to cart"

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

# Step 4: Click "Add to cart" for the Backpack, then click "Remove"
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
time.sleep(2)

# Step 5: Check the result
# Check 1: the red number on the cart icon should be gone
# (find_elements gives an empty list when nothing is found, no error)
badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
cart_ok = len(badges) == 0

# Check 2: the button should say "Add to cart" again
button_text = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").text
button_ok = button_text == "Add to cart"

if cart_ok and button_ok:
    print("PASS: Item removed. Cart is empty and button says", button_text)
else:
    print("FAIL: Cart badges found:", len(badges), "| Button says", button_text)

# Step 6: Close Chrome
time.sleep(2)
driver.quit()
