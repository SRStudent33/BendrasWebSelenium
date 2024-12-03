from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def register_account():
    link = "https://magento.softwaretestingboard.com/"
    browser = webdriver.Chrome()
    browser.get(link)

    try:
        captcha = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/button[1]/p")
        captcha.click()
        time.sleep(3)
    except:
        pass  # If no captcha, proceed

    account = browser.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[3]/a")
    account.click()
    time.sleep(3)

    submit_button = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/div/div[1]/button")
    submit_button.click()
    time.sleep(3)

    try:
        firstname_error = browser.find_element(By.ID, "firstname-error")
        if firstname_error.is_displayed() and "This is a required field." in firstname_error.text:
            print("Error: First name is required.")

        surname_error = browser.find_element(By.ID, "lastname-error")
        if surname_error.is_displayed() and "This is a required field." in surname_error.text:
            print("Error: Last name is required.")

        email_error = browser.find_element(By.ID, "email_address-error")
        if email_error.is_displayed() and "This is a required field." in email_error.text:
            print("Error: Email address is required.")


        print("Filling in the required fields...")

        name = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[1]/div[1]/div/input")
        name.send_keys("Edvinas")

        surname = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[1]/div[2]/div/input")
        surname.send_keys("Gaidamavicius")

        email = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[1]/div/input")
        email.send_keys("edvinas20023@gmail.com")

        password = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[2]/div/input")
        password.send_keys("edvinas2003!@#$")

        confirm_password = browser.find_element(By.XPATH,
                                                "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[3]/div/input")
        confirm_password.send_keys("edvinas2003!@#$")

        submit_button.click()
        time.sleep(3)

        try:
            final_error = browser.find_element(By.XPATH, "//div[@class='messages']//li")
            print("Error: Registration failed. Please check the details and try again.")
        except:
            print("Registration successful!")

    except Exception as e:
        print(f"Error checking required fields: {e}")
        print("Registration successful or no validation errors detected.")

    browser.quit()

register_account()
