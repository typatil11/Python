import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set the path to your ChromeDriver executable
chrome_driver_path = 'path/to/chromedriver.exe'

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Create a ChromeDriver instance
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

# Implicit Wait - Set a default waiting time for the entire script
driver.implicitly_wait(10)  # Wait for up to 10 seconds

driver.get("http://192.168.1.176:83/")

# Click on the cookie consent button
cookie_consent_button = driver.find_element(By.XPATH, '//*[@id="cookieConsent"]/div/button')
cookie_consent_button.click()

# Find the email input field using XPath and enter the email ID
email_input = driver.find_element(By.XPATH, '//input[@id="exampleInputEmail1"]')
email_input.send_keys("9000000008")

# Click on the email input field
email_input.click()

# Find the password input field using XPath and enter the password
password_input = driver.find_element(By.XPATH, '//input[@id="exampleInputPassword1"]')
password_input.send_keys("ProEx@2022")

# Add a delay of 10 seconds after entering the password
time.sleep(10)

# Find the captcha field using XPath and click on it
captcha_input = driver.find_element(By.XPATH, '//input[@id="CaptchaCode"]')
captcha_input.click()

# Add a delay of 2 seconds to see the changes
time.sleep(2)

# Find the toggle field using XPath and click on it
toggle_field = driver.find_element(By.XPATH, '//body/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/label[2]/span[1]/small[1]')
toggle_field.click()

# Add a delay of 2 seconds to see the changes
time.sleep(2)

# Find the submit button using XPath and click on it
submit_button = driver.find_element(By.XPATH, '//button[contains(text(),"Sign In")]')
submit_button.click()

# Add a delay of 2 seconds to see the changes
time.sleep(2)

# driver.quit()  # Close the browser window
