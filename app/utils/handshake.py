from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

PER_PAGE = 5  # FIXME - Optimize this number (50 is a good base)


class Result:
    def __init__(self):
        pass

    #     self.query = query
    #     self.test = "first"
    #     self.test2 = "second"

    # def __str__(self):
    #     return self.query + " " + self.test + " " + self.test2


def handshake(username, password, query, headless=False):
    result = Result()
    result.query = query
    result.test = "hello"
    # result.jobs_applied = ["java dev", "java developer"]

    # result.jobs_applied.append("hello")

    arr = ["java dev", "java developer"]
    arr.append("hello")

    result.jobs_applied = arr

    print("jobs", arr, result.jobs_applied)

    print("here we go")
    # start up web driver
    # chrome_options = Options()
    # if headless:
    #     print("running headless")
    #     chrome_options.add_argument("--headless")
    #     chrome_options.add_argument("--window-size=1920,1080")

    # driver = webdriver.Chrome(options=chrome_options)
    # driver.maximize_window()

    # # Convert spaces to '%20's for url
    # job_query = query.replace(" ", "%20")

    # # Go to search url (it will first redirect for auth)
    # driver.get(
    #     f"https://byu.joinhandshake.com/postings?page=1&per_page={PER_PAGE}&sort_direction=desc&sort_column=default&query={job_query}"
    # )

    # # Handle login

    # # Redirect to CAS BYU Login
    # byu_login_btn = driver.find_element(By.CLASS_NAME, "sso-button")
    # byu_login_btn.click()

    # # Fill in username, password, then sign in to BYU account

    # username_input = driver.find_element(By.ID, "username")
    # username_input.send_keys(username)

    # password_input = driver.find_element(By.ID, "password")
    # password_input.send_keys(password)

    # password_input.send_keys(Keys.ENTER)  # Press enter to submit login

    # # Give time to do DUO two-factor auth and redirect to postings page
    # sleep(20)

    # # Bypass the remember this computer screen
    # trust_browser_btn = driver.find_element(By.ID, "trust-browser-button")
    # if trust_browser_btn is None:
    #     print("You didn't authenticate with DUO in time")
    #     return
    # trust_browser_btn.click()

    # # Give time to finish bypass
    # sleep(20)

    # num_applies = 0  # Keeps track of how many times you applied successfully

    # jobs_applied = []  # Array containing jobs where you successfully applied

    # # Find all postings
    # print("finding postings")
    # postings = driver.find_elements(By.XPATH, "//a[@data-hook='jobs-card']")

    # # For each posting
    # for posting in postings:
    #     # Click on sidebar posting
    #     posting.click()
    #     sleep(2)

    #     # Grab name info
    #     posting_name = "?"
    #     posting_company = "?"
    #     posting_name_results = driver.find_elements(
    #         By.XPATH,
    #         '//*[@id="skip-to-content"]/div[3]/div/div[1]/div/form/div[2]/div/div/div[2]/div[1]/div[1]/h1/a',
    #     )
    #     if len(posting_name_results) == 1:
    #         posting_name = posting_name_results[0].text
    #     posting_company_results = driver.find_elements(
    #         By.XPATH,
    #         '//*[@id="skip-to-content"]/div[3]/div/div[1]/div/form/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/a',
    #     )
    #     if len(posting_company_results) == 1:
    #         posting_company = posting_company_results[0].text
    #     posting_headline = posting_name + " @ " + posting_company
    #     print(posting_headline)

    #     # Check if there's a 'Quick Apply' button
    #     apply_btn_results = driver.find_elements(
    #         By.XPATH, '//button/span/div[text()="Quick Apply"]'
    #     )
    #     has_quick_apply = True if len(apply_btn_results) > 1 else False

    #     if len(apply_btn_results) == 0:  # Check for normal apply if no luck
    #         apply_btn_results = driver.find_elements(
    #             By.XPATH, '//button/span/div[text()="Apply"]'
    #         )

    #     # If there is one
    #     if len(apply_btn_results) > 1:
    #         # Click Apply Button

    #         apply_btn = apply_btn_results[0]  # Grab the button from the list
    #         apply_btn.click()
    #         sleep(2)
    #         exit_posting_btn = (
    #             driver.find_element(  # Get exit number in case you need to get out
    #                 By.XPATH,
    #                 "/html/body/reach-portal/div[3]/div/div/div/span/div/button",
    #             )
    #         )

    #         # Click resume button (If it's not Quick Apply.  If it is quick apply, jump straight to submitting.)
    #         if not has_quick_apply:
    #             # Throw out 'Apply' types that aren't just resume
    #             # FIXME -- ADD CASE TO THROW OUT TOO SPECIFIC 'APPLY' types that ask for 'cover letter', 'transcript', anything more than resume

    #             # If there's no add resume button, skip over that posting
    #             add_resume_btn_results = driver.find_elements(
    #                 By.XPATH,
    #                 "/html/body/reach-portal/div[3]/div/div/div/span/form/div[1]/div/div[2]/fieldset/div/div[2]/span[1]/button",
    #             )
    #             if len(add_resume_btn_results) == 0:
    #                 exit_posting_btn.click()
    #                 continue  # Skip to next posting
    #             add_resume_btn = add_resume_btn_results[
    #                 0
    #             ]  # Grab the button from the list
    #             add_resume_btn.click()
    #             sleep(2)

    #         # Click 'Submit' Button

    #         submit_btn_results = driver.find_elements(
    #             By.XPATH, '//span/div/button/span[text()="Submit Application"]'
    #         )
    #         if len(submit_btn_results) == 0:
    #             exit_posting_btn.click()
    #             continue
    #         submit_btn = submit_btn_results[0]
    #         submit_btn.click()
    #         sleep(2)

    #         # Success cleanup

    #         jobs_applied.append(posting_headline)
    #         num_applies += 1  # Increment number of successful applies

    # print()
    # print("Done!")
    # # Close browser
    # driver.close()

    # print(
    #     "Successfully applied to",
    #     str(num_applies) + "/" + str(len(postings)),
    #     query,
    #     "jobs!",
    # )
    # for job in jobs_applied:
    #     print(job)
    # APP_RESULTS_URL = "https://byu.joinhandshake.com/applications?ref=account-dropdown"
    # print(f"Visit {APP_RESULTS_URL} for details on where you applied.")

    return result
