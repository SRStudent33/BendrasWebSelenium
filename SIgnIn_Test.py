import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

# URL and element locators
LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2xvZ291dFN1Y2Nlc3Mv/"
PRODUCT_URL = "https://magento.softwaretestingboard.com/ajax-full-zip-sweatshirt.html"
LOGIN_BUTTON = "send2"
SIGN_IN_ERROR_MESSAGE = "//*[@id='maincontent']/div[2]/div[2]/div/div"
ERROR_MESSAGE = "//*[@id='maincontent']/div[1]/div[2]/div/div[1]"
PRIVACY_POPUP = "fc-button-label"
REVIEW_BUTTON = "tab-label-reviews-title"
SUBMIT_REVIEW_BUTTON = "//*[@id='review-form']/div/div/button"
REVIEW_ERROR_MESSAGE = "//*[@id='maincontent']/div[1]/div[2]/div/div[1]"
REVIEW_NICKNAME_FIELD = "nickname_field"
REVIEW_SUMMARY_FIELD = "summary_field"
REVIEW_FIELD = "review_field"
REVIEW_STAR_1 = "//label[@id='Rating_1_label']"
REVIEW_STAR_2 = "Rating_2_label"
REVIEW_STAR_3 = "Rating_3_label"
REVIEW_STAR_4 = "Rating_4_label"
REVIEW_STAR_5 = "Rating_5_label"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_sign_in_with_correct_credentials(browser):
    """Test signing in with correct credentials."""
    email = "hawk@gmail.com"  #Valid credentials
    password = "Fancy123"

    browser.get(LOGIN_URL)
    browser.find_element(By.CLASS_NAME, PRIVACY_POPUP).click()
    browser.find_element(By.ID, "email").send_keys(email)
    browser.find_element(By.ID, "pass").send_keys(password)
    browser.find_element(By.ID, LOGIN_BUTTON).click()

    WebDriverWait(browser, 10).until(EC.url_changes(LOGIN_URL))

def test_sign_in_with_random_credentials(browser):
    """Test signing in with random credentials."""
    email = ''.join(random.choices(string.ascii_lowercase, k=8)) + "@example.com"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

    browser.get(LOGIN_URL)
    browser.find_element(By.CLASS_NAME, PRIVACY_POPUP).click()
    browser.find_element(By.ID, "email").send_keys(email)
    browser.find_element(By.ID, "pass").send_keys(password)
    browser.find_element(By.ID, LOGIN_BUTTON).click()

    error_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, SIGN_IN_ERROR_MESSAGE))
    ).text


def test_sign_in_with_empty_fields(browser):
    """Test signing in with empty fields."""
    browser.get(LOGIN_URL)
    browser.find_element(By.CLASS_NAME, PRIVACY_POPUP).click()
    browser.find_element(By.ID, LOGIN_BUTTON).click()

    error_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, SIGN_IN_ERROR_MESSAGE))
    ).text


def test_leave_review_with_empty_fields(browser):
    """Test leaving a review with empty fields."""
    browser.get(PRODUCT_URL)
    browser.find_element(By.CLASS_NAME, PRIVACY_POPUP).click()
    browser.find_element(By.ID, REVIEW_BUTTON).click()
    browser.find_element(By.XPATH, SUBMIT_REVIEW_BUTTON).click()
    error_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, ERROR_MESSAGE))
    ).text

def test_leave_review_nickname_as_numbers(browser):
    """Test leaving a review with nickname as numbers."""
    browser.get(PRODUCT_URL)
    browser.find_element(By.CLASS_NAME, PRIVACY_POPUP).click()
    browser.find_element(By.ID, REVIEW_BUTTON).click()
    time.sleep(2)
    browser.find_element(By.XPATH, REVIEW_STAR_1).click()
    browser.find_element(By.ID, REVIEW_NICKNAME_FIELD).send_keys("458246")
    time.sleep(1)
    browser.find_element(By.ID, REVIEW_SUMMARY_FIELD).send_keys("asdasd")
    time.sleep(1)
    browser.find_element(By.ID, REVIEW_FIELD).send_keys("asdasdsad")

def test_leave_review_no_stars(browser):
    """Test leaving a review with 0 stars"""
    browser.get(PRODUCT_URL)
    browser.find_element(By.CLASS_NAME, PRIVACY_POPUP).click()
    browser.find_element(By.ID, REVIEW_BUTTON).click()
    time.sleep(1)
    browser.find_element(By.ID, REVIEW_NICKNAME_FIELD).send_keys("Hero")
    time.sleep(1)
    browser.find_element(By.ID, REVIEW_SUMMARY_FIELD).send_keys("cool")
    time.sleep(1)
    browser.find_element(By.ID, REVIEW_FIELD).send_keys("LOREM IPSUM")

