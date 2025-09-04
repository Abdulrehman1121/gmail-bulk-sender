import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Load email IDs from CSV
csv_file = "MAIL IDS.csv"  # Replace with your actual CSV file
df = pd.read_csv(csv_file)

# Convert email column to list
recipient_emails = df['email'].tolist()  # Change column name if needed

# Email subject and body
subject = "Your subject here"
body = f""" your email here
"""

# Attach to an existing Chrome session
options = webdriver.ChromeOptions()
options.debugger_address = "localhost:9222"  # Port where existing Chrome is running

driver = webdriver.Chrome(options=options)
driver.get("https://mail.google.com/")

# Wait until the Gmail compose button is available (indicating Gmail is fully loaded)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Compose')]")))

# Send emails
for email in recipient_emails:
    try:
        # Click Compose button
        compose_button = driver.find_element(By.XPATH, "//div[contains(text(),'Compose')]")
        compose_button.click()

        # Wait for the "To" field to be interactable (Compose window open and ready)
        to_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='To recipients']")))

        # Ensure the field is cleared (sometimes it has previous content)
        to_field.clear()

        # Enter recipient email
        driver.execute_script("arguments[0].scrollIntoView();", to_field)  # Scroll if needed
        to_field.send_keys(email)
      
        # Wait for dropdown and select the first suggestion
        time.sleep(1)  # Small delay to allow the dropdown to appear
        to_field.send_keys(Keys.ARROW_DOWN)  # Select the first suggestion
        to_field.send_keys(Keys.ENTER)  # Confirm 
        


        # Wait and enter the subject
        subject_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "subjectbox")))
        subject_field.send_keys(subject)

        # Wait and enter the email body
        body_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Message Body']")))
        body_field.send_keys(body)
        time.sleep(3)  # Wait for the body to be fully entered
        # Wait for and click the send button
        body_field.send_keys(Keys.CONTROL, Keys.ENTER)

        # send_button = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.XPATH, "//div[@role='button' and contains(text(), 'Send')]")))
        # driver.execute_script("arguments[0].click();", send_button)



        print(f"Email sent to {email}")

        # Wait for the next email to be ready to send
        time.sleep(3)  # Pause between emails to avoid rate limits

    except Exception as e:
        print(f"Error sending email to {email}: {str(e)}")

print("All emails sent successfully!")

# Do not close the browser to keep session active
