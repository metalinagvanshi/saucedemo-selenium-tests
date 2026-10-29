# Playwright version of Test 1: Login with correct username and password
# Expected result: the "Products" page should open
# Same test as test1_login.py, written with Playwright to compare it with Selenium.
# Playwright waits for elements by itself, so no time.sleep is needed.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Step 1: Open Chromium (headless=False so we can see it)
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # Step 2: Go to the demo shopping website
    page.goto("https://www.saucedemo.com")

    # Step 3: Type username and password, then click Login
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Step 4: Check the result
    title = page.locator(".title").text_content()
    if title == "Products":
        print("PASS: Login worked, Products page opened")
    else:
        print("FAIL: Expected 'Products' but got:", title)

    # Step 5: Close the browser
    browser.close()
