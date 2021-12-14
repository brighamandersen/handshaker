import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Check cmd line args (need to pass in job description)
job_query = "Front End Developer"

# Grab up env vars
BYU_USERNAME = os.environ.get("BYU_USERNAME")
BYU_PASSWORD = os.environ.get("BYU_PASSWORD")

# start up web driver
driver = webdriver.Chrome()

# Try to go to posting page (it will redirect here after login)
driver.get("https://byu.joinhandshake.com/postings")

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

# Type in search
job_search_input = driver.find_element(By.ID, "quick-filters-query")
job_search_input.send_keys(job_query)
job_search_input.send_keys(Keys.ENTER)

# Grab postings
postings = driver.find_elements(By.xpath("//a[@data-hook='jobs-card']"))
print(postings)
print(len(postings))
