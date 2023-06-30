import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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

# Find the "Warehouse" field using XPath and click on it
warehouse_field = driver.find_element(By.XPATH, '//span[contains(text(),"Warehouse")]')
warehouse_field.click()

time.sleep(2)

# Find the "add-warehouse" field using XPath and click on it
add_warehouse_field = driver.find_element(By.XPATH, '//header/div[2]/a[2]/span[1]/span[1]/i[1]')
add_warehouse_field.click()

# Find the "shortname" field using XPath, click on it, and send the value "TestWarehouse" to it
shortname_field = driver.find_element(By.XPATH, '//input[@id="Locshortname"]')
shortname_field.click()
shortname_field.send_keys("TestWarehouse")

# Find the "warehouse_name" field using XPath, click on it, and send the value "TestDemo" to it
warehouse_name_field = driver.find_element(By.XPATH, '//input[@id="Locname"]')
warehouse_name_field.click()
warehouse_name_field.send_keys("TestDemo")

# Find the "save_war" button using XPath and click on it
save_war_button = driver.find_element(By.XPATH, '//button[contains(text(),"Save")]')
save_war_button.click()

time.sleep(2)
