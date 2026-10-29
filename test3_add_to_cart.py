# Test 3: Add one item to the cart
# Expected result: cart icon shows "1", and the button changes to "Remove"

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

# Step 4: Click "Add to cart" for the Backpack
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)

# Step 5: Check the result
# Check 1: the red number on the cart icon should be "1"
cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
cart_ok = cart_count == "1"

# Check 2: the button should now say "Remove"
button_text = driver.find_element(By.ID, "remove-sauce-labs-backpack").text
button_ok = button_text == "Remove"

if cart_ok and button_ok:
    print("PASS: Item added. Cart shows", cart_count, "and button says", button_text)
else:
    print("FAIL: Cart shows", cart_count, "| Button says", button_text)

# Step 6: Close Chrome
time.sleep(2)
driver.quit()
