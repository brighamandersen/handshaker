import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--query", type=str, help="Job search query", required=True)
args = parser.parse_args()

PER_PAGE = 50  # FIXME - Optimize this number

# Convert spaces to '%20's for url
raw_job_query = args.query
job_query = raw_job_query.replace(" ", "%20")

# Grab up env vars
BYU_USERNAME = os.environ.get("BYU_USERNAME")
BYU_PASSWORD = os.environ.get("BYU_PASSWORD")

# start up web driver
driver = webdriver.Chrome()

# Go to search url (it will first redirect for auth)
driver.get(
    f"https://byu.joinhandshake.com/postings?page=1&per_page={PER_PAGE}&sort_direction=desc&sort_column=default&query={job_query}"
)

# Handle login

# Redirect to CAS BYU Login
byu_login_btn = driver.find_element(By.CLASS_NAME, "sso-button")
byu_login_btn.click()

# Fill in username, password, then sign in to BYU account

username_input = driver.find_element(By.ID, "username")
username_input.send_keys(BYU_USERNAME)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(BYU_PASSWORD)

password_input.send_keys(Keys.ENTER)  # Press enter to submit login

# Give time to do DUO two-factor auth and redirect to postings page
sleep(25)

num_applies = 0  # Keeps track of how many times you applied successfully

# Find all postings
postings = driver.find_elements(By.XPATH, "//a[@data-hook='jobs-card']")

# For each posting
for posting in postings:
    posting_name = driver.find_element(
        By.XPATH,
        '//*[@id="skip-to-content"]/div[3]/div/div[1]/div/form/div[2]/div/div/div[2]/div[1]/div[1]/h1/a',
    ).text
    posting_company = driver.find_element(
        By.XPATH,
        '//*[@id="skip-to-content"]/div[3]/div/div[1]/div/form/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/a',
    ).text
    print(posting_name, "@", posting_company)

    # Click on sidebar posting
    posting.click()
    sleep(2)

    # Check if there's a 'Quick Apply' button
    apply_button_results = driver.find_elements(
        By.XPATH, '//button/span/div[text()="Quick Apply"]'
    )
    if len(apply_button_results) == 0:  # Check for normal apply if no luck
        apply_button_results = driver.find_elements(
            By.XPATH, '//button/span/div[text()="Apply"]'
        )

    # If there is one
    if len(apply_button_results) > 1:

        # Click Apply Button

        apply_button = apply_button_results[0]  # Grab the button from the list
        apply_button.click()
        exit_posting_btn = (
            driver.find_element(  # Get exit number in case you need to get out
                By.XPATH, "/html/body/reach-portal/div[3]/div/div/div/span/div/button"
            )
        )
        sleep(2)

        # Click resume button

        add_resume_btn_results = driver.find_elements(
            By.XPATH,
            "/html/body/reach-portal/div[3]/div/div/div/span/form/div[1]/div/div[2]/fieldset/div/div[2]/span[1]/button",
        )
        # If there's no add resume button, skip over that posting
        if len(add_resume_btn_results) == 0:
            exit_posting_btn.click()
            continue  # Skip to next posting
        add_resume_btn = add_resume_btn_results[0]  # Grab the button from the list
        add_resume_btn.click()
        sleep(2)

        # Click 'Submit' Button

        submit_btn_results = driver.find_elements(
            By.XPATH, '//span/div/button[text()="Submit Application"]'
        )
        if len(submit_btn_results) == 0:
            exit_posting_btn.click()
            continue
        submit_btn = submit_btn_results[0]
        # submit_btn = driver.find_element(
        #     By.XPATH,
        #     "/html/body/reach-portal/div[3]/div/div/div/span/form/div[2]/div/span/div/button",
        # )
        submit_btn.click()
        sleep(2)

        # Increment number of successful applies
        num_applies += 1

# Close browser
driver.close()

print(
    "Successfully applied to",
    str(num_applies) + "/" + str(len(postings)),
    raw_job_query,
    "jobs!",
)
APP_RESULTS_URL = "https://byu.joinhandshake.com/applications?ref=account-dropdown"
print(f"Visit {APP_RESULTS_URL} for details on where you applied.")
