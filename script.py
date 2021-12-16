import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--query", type=str, help="Job search query", required=True)
args = parser.parse_args()

# Convert spaces to '%20's for url
job_query = args.query.replace(" ", "%20")

# Grab up env vars
BYU_USERNAME = os.environ.get("BYU_USERNAME")
BYU_PASSWORD = os.environ.get("BYU_PASSWORD")

# start up web driver
driver = webdriver.Chrome()

# Go to search url (it will first redirect for auth)
driver.get(
    f"https://byu.joinhandshake.com/postings?page=1&per_page=1000&sort_direction=desc&sort_column=default&query={job_query}"
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
sleep(30)

# Once redirected back to search, then grab all postings
# postings = driver.find_elements(By.xpath("//a[@data-hook='jobs-card']"))
postings = driver.find_element(By.cssSelector("a[data-hook='jobs-card']"))
print(postings)
print(len(postings))
