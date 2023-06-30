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

driver.get("http://192.168.1.176:83/")

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

# Find the "Masters" field using XPath and click on it
masters_field = driver.find_element(By.XPATH, '//span[contains(text(),"Masters")]')
masters_field.click()

time.sleep(2)

# Find the "Buyer" field using XPath and click on it
buyer_field = driver.find_element(By.XPATH, '//span[contains(text(),"Agent")]')
buyer_field.click()

time.sleep(2)

# Find the "Add Buyer" field using XPath and click on it
add_buyer_field = driver.find_element(By.XPATH, '//header/div[2]/a[2]/span[1]/span[1]/i[1]')
add_buyer_field.click()

time.sleep(2)

# Find the "Name" field using XPath and enter the value
name_field = driver.find_element(By.XPATH, '//input[@id="Name"]')
name_field.send_keys("testuser1")

# Find the "Mobile No" field using XPath and enter the value
mobile_field = driver.find_element(By.XPATH, '//input[@id="Mob"]')
mobile_field.send_keys("65465465")

# Find the "Email ID" field using XPath and enter the value
email_field = driver.find_element(By.XPATH, '//input[@id="Email"]')
email_field.send_keys("testing@naapbooks.com")

# Find the "Credit Limit" field using XPath and enter the value
credit_limit_field = driver.find_element(By.XPATH, '//input[@id="Creditlimit"]')
credit_limit_field.send_keys("10000")

opening_balance = driver.find_element(By.XPATH, '//input[@id="Openingbalance"]')
opening_balance.send_keys('1000')

# Find the "Current Balance" field using XPath and enter the value
current_balance_field = driver.find_element(By.XPATH, '//input[@id="Currentbalance"]')
current_balance_field.send_keys("100")

# Find the "Group Name" field using XPath and click on it
group_name_field = driver.find_element(By.XPATH, '//span[@id="select2-Groupid-container"]')
group_name_field.click()

group_name_search = driver.find_element(By.XPATH, '//body/span[1]/span[1]/span[1]/input[1]')
group_name_search.click()
group_name_search.send_keys('pay')
group_name_search.send_keys(Keys.ENTER)

time.sleep(2)

# Find the "Group Name" field using XPath and click on it
group_name_field = driver.find_element(By.XPATH, '//span[@id="select2-Groupid-container"]')
group_name_field.click()

# Find the search input field within the dropdown and click on it
search_input = driver.find_element(By.XPATH, '//input[@class="select2-search__field"]')
search_input.click()

# Send keys "Proex" to the search input field
search_input.send_keys("Proex")

# Send the Enter key to select the option
search_input.send_keys(Keys.ENTER)

# Find the "GST No" field using XPath and enter the value
gst_no_field = driver.find_element(By.XPATH, '//input[@id="gstno"]')
gst_no_field.send_keys("18AABCU9603R1ZM")

# Find the "Bank" field using XPath and click on it
bank_field = driver.find_element(By.XPATH, '//span[@id="select2-Bankid-container"]')
bank_field.click()

# Find the search input field within the dropdown and click on it
bank_search_input = driver.find_element(By.XPATH, '//body/span[1]/span[1]/span[1]/input[1]')
bank_search_input.click()

# Send keys "jalgaon janta bank" to the search input field
bank_search_input.send_keys("jalgaon janata")

# Send the Enter key to select the option
bank_search_input.send_keys(Keys.ENTER)

# Find the "Account No" field using XPath and enter the value
account_no_field = driver.find_element(By.XPATH, "//input[@id='Bankaccountno']")
account_no_field.send_keys("34252012267")

# Find the "IFSC Code" field using XPath and enter the value
ifsc_code_field = driver.find_element(By.XPATH, "//input[@id='Bankifsccode']")
ifsc_code_field.send_keys("SBIN0000393")

# Scroll down the page until the "Address" field is visible
address_field = driver.find_element(By.XPATH, '//input[@id="Custaddresses_0__Address"]')
driver.execute_script("arguments[0].scrollIntoView();", address_field)

# Find the "Address" field using XPath and enter the value
address_field.send_keys("BBC building")

# Find the "Pincode" field using XPath and enter the value
pincode_field = driver.find_element(By.XPATH, '//input[@id="Custaddresses_0__Pincode"]')
pincode_field.send_keys("425001")
# Find the dropdown element using XPath
# Find the dropdown element using XPath
dropdown = driver.find_element(By.XPATH, '//span[@id="select2-Custaddresses_0__Country-container"]')

# Click on the dropdown to open the options
dropdown.click()

# Find the search input field within the dropdown and enter the search text
search_input = driver.find_element(By.XPATH, '//body/span[1]/span[1]/span[1]/input[1]')
search_input.send_keys("India")

# Wait for the options to be visible
wait = WebDriverWait(driver, 10)
options = wait.until(
    EC.visibility_of_all_elements_located((By.XPATH, '//ul[@id="select2-Custaddresses_0__Country-results"]/li')))

# Iterate through the options and select the desired one
for option in options:
    if option.text == "India":
        option.click()
        break

# Find the "State" field using XPath and click on it
state_field = driver.find_element(By.XPATH, '//span[@id="select2-Custaddresses_0__State-container"]')
state_field.click()


# Find the search input field within the dropdown and enter the search text
state_search_input = driver.find_element(By.XPATH, '//body/span[1]/span[1]/span[1]/input[1]')
state_search_input.send_keys("Gujarat")

# Press Enter to select the option
state_search_input.send_keys(Keys.ENTER)

# Find the "City" field using XPath and enter the value
city_field = driver.find_element(By.XPATH, '//input[@id="Custaddresses_0__City"]')
city_field.send_keys("Ahmedabad")

# Find the "Contact Name" field using XPath and enter the value
contact_name_field = driver.find_element(By.XPATH, '//input[@id="Custauthpeople_0__Name"]')
contact_name_field.send_keys("Contact Demo")

# Find the "Contact Mobile" field using XPath and enter the value
con_mobile_field = driver.find_element(By.XPATH, '//input[@id="Custauthpeople_0__Mobno"]')
con_mobile_field.send_keys("3216549871")

save_field = driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()
