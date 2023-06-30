import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your ChromeDriver executable
chrome_driver_path = 'path/to/chromedriver.exe'

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Create a ChromeDriver instance
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

# Implicit Wait - Set a default waiting time for the entire script
driver.implicitly_wait(10)  # Wait for up to 10 seconds

driver.get("https://bgs-uat.naapbooks.com/")

# Find the email input element using XPath
email_input = driver.find_element(By.XPATH, '//input[@id="EmailId"]')

# Explicit Wait - Wait until the email input field is visible
wait = WebDriverWait(driver, 10)
email_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="EmailId"]')))

# Find the password input element using XPath
password_input = driver.find_element(By.XPATH, '//input[@id="txtPassword"]')

# Find the login button using XPath
login_button = driver.find_element(By.XPATH, '//button[contains(text(),"Login")]')

# Now you can interact with the email, password, and login button

# To send keys (input text) to the email input field:
email_input.send_keys("lareb@gmail.com")

# To send keys (input text) to the password input field:
password_input.send_keys("123456")

# To click on the login button:
login_button.click()

time.sleep(1)

# Find the "Inventory" field using XPath and click on it
inventory_field = driver.find_element(By.XPATH, '//span[contains(text(),"Inventory")]')
inventory_field.click()

item = driver.find_element(By.XPATH, '//*[@id="dash_inv"]/li/ul/li[4]/a/span')
item.click()

add_buyer_field = driver.find_element(By.XPATH, '//header/div[2]/a[2]/span[1]/span[1]/i[1]')
add_buyer_field.click()

time.sleep(5)
file_input = driver.find_element(By.XPATH, '//input[@id="formFile"]')
# Specify the file path to upload
file_path = 'F:\arihant\asset\img'  # Replace with the actual file path on your system

# Use the send_keys method to upload the file
file_input.send_keys(file_path)

# Submit the form or perform any other necessary actions
submit_button = driver.find_element(By.ID, 'submit-button')
submit_button.click()

# Add a delay or use WebDriverWait as needed to wait for the file upload to complete

# driver.quit()  # Close the browser window
