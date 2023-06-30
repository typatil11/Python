import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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

driver.get("http://192.168.1.176:99/")

# Rest of your code...

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
buyer_field = driver.find_element(By.XPATH, '//span[contains(text(),"Employee")]')
buyer_field.click()

add_buyer_field = driver.find_element(By.XPATH, '//header/div[2]/a[2]/span[1]/span[1]/i[1]')
add_buyer_field.click()


# Find the "New_employee" field using XPath and send the value "testEmp" to it
new_employee_field = driver.find_element(By.XPATH, '//input[@id="Name"]')
new_employee_field.send_keys("testEmp")

# Find the "Email_id" field using XPath and send the value "test1@gmail.com" to it
email_id_field = driver.find_element(By.XPATH, '//input[@id="Emailid"]')
email_id_field.send_keys("test1@gmail.com")

# Find the "password" field using XPath and send the value "ProEx@2013" to it
password_field = driver.find_element(By.XPATH, '//input[@id="txtPassword"]')
password_field.send_keys("ProEx@2013")

# Find the "personal_mobile no" field using XPath and send the value "9874124575" to it
personal_mobile_field = driver.find_element(By.XPATH, '//input[@id="Contactno"]')
personal_mobile_field.send_keys("9874124575")

# Find the "gender" field using XPath and click on it to open the dropdown menu
gender_field = driver.find_element(By.XPATH, '//span[@id="select2-Genderid-container"]')
gender_field.click()

# Wait for the search field in the gender dropdown to be visible and send the keys "male" to it. Then send the "Enter" key to select the option
search_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//body/span[1]/span[1]/span[1]/input[1]')))
search_field.send_keys("male")
search_field.send_keys(Keys.ENTER)

# Find the "adhar card" field using XPath and send the value "210947177276" to it
adhar_card_field = driver.find_element(By.XPATH, '//input[@id="Aadharid"]')
adhar_card_field.send_keys("210947177276")

# Find the "pancard" field using XPath and send the value "EULPP121D" to it
pancard_field = driver.find_element(By.XPATH, '//input[@id="Panid"]')
pancard_field.send_keys("EULPP1213D")

# Rest of your code...



# Scroll to the "Save_employee" element using ActionChains
save_employee_button = driver.find_element(By.XPATH, '//button[contains(text(),"Save")]')
actions = ActionChains(driver)
actions.move_to_element(save_employee_button).perform()
time.sleep(2)
# Click on the "Save_employee" button
save_employee_button.click()

time.sleep(2)

rows = driver.find_elements_by_xpath('//*[@id="datable_4c"]/tbody/tr')

# Iterate over the rows
for row in rows[:3]:  # Limit to 3 rows
    # Find all the columns within each row
    columns = row.find_elements_by_xpath("//*[@id='datable_4c']/tbody/tr[1]/td")

    # Check if the row has the desired number of columns
    if len(columns) == 6:  # Limit to 6 columns
        # Iterate over the columns
        for column in columns:
            # Print the text content of each column
            print(column.text)

        # Add a new line after each row
        print()

# Close the browser
driver.quit()