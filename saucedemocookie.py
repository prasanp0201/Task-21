from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (make sure to have the appropriate driver installed)
driver = webdriver.Chrome()

try:
    # Open the webpage
    driver.get("https://www.saucedemo.com/")
    
    # Display cookies before login
    cookies_before_login = driver.get_cookies()
    print("Cookies before login:")
    for cookie in cookies_before_login:
        print(cookie)

    # Perform login
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Use the provided standard user credentials
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    # Wait for the dashboard page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    # Display cookies after login
    cookies_after_login = driver.get_cookies()
    print("\nCookies after login:")
    for cookie in cookies_after_login:
        print(cookie)

    # Perform logout
    menu_button = wait.until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
    menu_button.click()
    
    logout_link = wait.until(EC.presence_of_element_located((By.ID, "logout_sidebar_link")))
    logout_link.click()

    # Display cookies after logout
    cookies_after_logout = driver.get_cookies()
    print("\nCookies after logout:")
    for cookie in cookies_after_logout:
        print(cookie)

finally:
    # Close the WebDriver
    driver.quit()
