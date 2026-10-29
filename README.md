# SauceDemo test automation (Selenium + Python)

A small UI test automation project on the demo shopping site [saucedemo.com](https://www.saucedemo.com), written while learning software testing. It has 5 Selenium tests (positive and negative) and 1 Playwright test to compare the two tools.

## Tests

| # | File | What it checks | Type |
|---|---|---|---|
| 1 | `test1_login.py` | Correct username and password opens the Products page | Positive |
| 2 | `test2_wrong_password.py` | Wrong password keeps the user on the login page and shows an error | Negative |
| 3 | `test3_add_to_cart.py` | Adding an item shows "1" on the cart and the button changes to "Remove" | Positive |
| 4 | `test4_remove_from_cart.py` | Removing the item clears the cart and the button changes back to "Add to cart" | Positive |
| 5 | `test5_checkout.py` | Full checkout ends on the "Thank you for your order!" page | End-to-end |
| - | `playwright_test1_login.py` | Test 1 written again with Playwright | Comparison |

Every test follows the same pattern: **Setup** (open browser, log in) → **Action** → **Check** (expected vs actual) → **Close**.

## How to run

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python test1_login.py
```

Each test prints `PASS` or `FAIL`.

## Locators used

ID (`user-name`, `login-button`), class name (`title`, `shopping_cart_badge`) and CSS selector (`[data-test='error']`).

## Selenium vs Playwright (what I noticed)

- Selenium needed `time.sleep` between steps; Playwright waits for elements by itself.
- Playwright code is shorter (`page.fill`, `page.click`).
- Selenium supports more languages and browsers and is the long-time industry standard.

A fuller comparison with Cypress, WebdriverIO, Robot Framework, Katalon, Appium and Postman is in [ALTERNATIVES.md](ALTERNATIVES.md).

## Bugs found and logged in JIRA

While testing other SauceDemo users I logged these bugs in JIRA (steps, expected vs actual, severity, priority, screenshot):

1. `problem_user`: every product shows the same image. (Medium)
2. `problem_user`: typing in Last Name on checkout goes into First Name. (High)
3. `performance_glitch_user`: login takes about 5 seconds. (Medium)

## Next steps

- Replace `time.sleep` with explicit waits (`WebDriverWait`)
- Move the tests to PyTest with `assert`
- Use the Page Object Model
