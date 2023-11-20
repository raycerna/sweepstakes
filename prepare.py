from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import schedule
import time

def fill_grabagun_sweepstakes_form(first_name, last_name, email, phone_number, address, city, state, zip_code):
    driver = webdriver.Chrome()
    driver.get("https://grabagun.com/giveaway")

    # Pause for a couple of seconds (e.g., 10 seconds) so that the webpage loads.
    time.sleep(10)

    # Waits for the "Yes" button to be clickable. Then selects "Yes" for over 21 years of age.
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Yes')]"))).click()

    # Pauses for a couple of seconds (e.g., 10 seconds)
    time.sleep(10)

    # Waits for the first name field to be present.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first_name")))

    # Fills in the first name
    driver.find_element(By.ID, "first_name").send_keys(first_name)

    # Waits for the last name field to be present.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "last_name")))

    # Fills in the last name
    driver.find_element(By.ID, "last_name").send_keys(last_name)

    # Waits for the email field to be present.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

    # Fills in the email
    driver.find_element(By.ID, "email").send_keys(email)

    # Waits for the phone number field to be present.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "telephone")))

    # Fills in the phone number
    driver.find_element(By.ID, "telephone").send_keys(phone_number)

    # Waits for the street field to be present.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "street")))

    # Fills in the address
    driver.find_element(By.ID, "street").send_keys(address)

    # Wait for the city field to be present.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "city")))

    # Fills in the city
    driver.find_element(By.ID, "city").send_keys(city)

    # Wait for the state dropdown to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "state")))

    # Selects the state from the dropdown
    select_state = Select(driver.find_element(By.ID, "state"))
    select_state.select_by_visible_text(state)

    # Wait for the zip code field to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "zip_code")))

    # Fills in the zip code
    driver.find_element(By.ID, "zip_code").send_keys(zip_code)

    # Waits for the terms and conditions checkbox to be present.
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "terms_and_conditions")))

    # Clicks the terms and conditions checkbox.
    driver.find_element(By.ID, "terms_and_conditions").click()

    # Waits for the Sign Up button to be clickable.
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "send2")))

    # Clicks the Sign Up button.
    driver.find_element(By.ID, "send2").click()

    # Pauses for a couple of seconds (e.g., 10 seconds)
    time.sleep(10)

    # Closes the Chrome browser.
    driver.quit()

# Example usage:
fill_grabagun_sweepstakes_form("Carlos", "Hathcock", "carloshathcock@gmail.com", "555-555-5555", "125 S FRONT ST", "Philadelphia", "Pennsylvania", "19106")

# Schedule the function to run every 6 hours.
# You can only run it in this interval for this sweepstakes.
schedule.every(6).hours.do(fill_grabagun_sweepstakes_form, "Carlos", "Hathcock", "carloshathcock@gmail.com", "555-555-5555", "125 S FRONT ST", "Philadelphia", "Pennsylvania", "19106")

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
