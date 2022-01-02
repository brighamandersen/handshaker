import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--query", type=str, help="Job search query", required=True)
args = parser.parse_args()

PER_PAGE = 10  # FIXME - Change

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

# Once redirected back to search, then grab all postings
# postings = driver.find_elements(By.xpath("//a[@data-hook='jobs-card']"))
# postings = driver.find_element(By.cssSelector("a[data-hook='jobs-card']"))

# postings = driver.find_elements(
#     By.XPATH, "//body[contains(@class, 'style__card-content')]"
# )
########


# Find all postings
postings = driver.find_elements(By.XPATH, "//a[@data-hook='jobs-card']")
print(postings)
print("Number of postings is", len(postings))

# For each posting
for posting in postings:

    # Click on sidebar posting
    posting.click()
    sleep(3)

    # Check if there's an 'Apply' button
    quick_apply_button_results = driver.find_elements(
        By.XPATH, '//button/span/div[text()="Apply"]'
    )
    if len(quick_apply_button_results) == 0:  # Check for quick apply if no luck
        quick_apply_button_results = driver.find_elements(
            By.XPATH, '//button/span/div[text()="Quick Apply"]'
        )
    print("qa", quick_apply_button_results)

    # If there is one
    if len(quick_apply_button_results) > 1:

        # Click 'Quick Apply' Button
        quick_apply_button = quick_apply_button_results[
            0
        ]  # Grab the button from the list
        quick_apply_button.click()
        sleep(3)

        # FIXME -- Maybe check here that there's only 1 step

        # Click resume button
        add_resume_btn = driver.find_element(
            By.XPATH,
            "/html/body/reach-portal/div[3]/div/div/div/span/form/div[1]/div/div[2]/fieldset/div/div[2]/span[1]/button",
        )
        add_resume_btn.click()
        sleep(3)

        # Click 'Submit' Button
        submit_btn = driver.find_element(
            By.XPATH,
            "/html/body/reach-portal/div[3]/div/div/div/span/form/div[2]/div/span/div/button",
        )
        submit_btn.click()
        sleep(3)

        # Increment number of successful applies
        num_applies += 1

# Close browser
driver.close()

print("Successfully applied to", num_applies, raw_job_query, "jobs!")
APP_RESULTS_URL = "https://byu.joinhandshake.com/applications?ref=account-dropdown"
print(f"Visit {APP_RESULTS_URL} for details on where you applied.")
