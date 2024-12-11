import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL and element locators
WALK_THRU = "https://magento.softwaretestingboard.com/"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def scroll_down_slowly(browser, scroll_amount, delay, duration):
    """
    Scrolls down the page slowly.

    :param browser: WebDriver instance
    :param scroll_amount: Amount to scroll in each step (pixels)
    :param delay: Delay between scrolls (seconds)
    :param duration: Total time to scroll (seconds)
    """

    start_time = time.time()

    while time.time() - start_time < duration:
        browser.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(delay)

def test_women_section_walk_thru(browser):
    """Testing women Tops/Bottoms sections"""
    browser.get(WALK_THRU)
    time.sleep(1)
    browser.find_element(By.ID, "ui-id-4").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul[1]/li[1]/a").click()

    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul[1]/li[2]/a").click()
    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul[1]/li[3]/a").click()
    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul[2]/li[1]/a").click()
    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul[2]/li[2]/a").click()
    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

def test_men_section_walk_thru(browser):
    browser.get(WALK_THRU)
    time.sleep(1)
    browser.find_element(By.ID, "ui-id-5").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul[1]/li[1]/a").click()

    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul[1]/li[2]/a").click()
    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul[1]/li[3]/a").click()
    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul[2]/li[1]/a").click()
    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul[2]/li[2]/a").click()
    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

def test_gear_section_walk_thru(browser):
    browser.get(WALK_THRU)
    time.sleep(1)
    browser.find_element(By.ID, "ui-id-6").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul/li[1]/a").click()

    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul/li[1]/a").click()
    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

    browser.find_element(By.XPATH, "/html/body/div[2]/main/div[4]/div[2]/div[2]/div/ul/li[3]/a").click()
    scroll_down_slowly(browser, scroll_amount=2, delay=0.01, duration=8)
    browser.back()
    time.sleep(2)

def test_on_advanced_search(browser):
    browser.get(WALK_THRU)
    time.sleep(1)
    scroll_down_slowly(browser, scroll_amount=2, delay=0.001, duration=8)
    browser.find_element(By.XPATH, "/html/body/div[2]/footer/div/ul/li[3]/a").click()
    time.sleep(2)
    Name = browser.find_element(By.ID, "name").send_keys("Yoga")
    time.sleep(1)
    SKU = browser.find_element(By.ID, "sku").send_keys("24-WG084")
    time.sleep(1)
    Price = browser.find_element(By.ID, "price").send_keys("1")
    time.sleep(1)
    Price_to = browser.find_element(By.ID, "price_to").send_keys("10")
    time.sleep(1)
    Submit = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/div/div/button").click()
    time.sleep(2)
    Product = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div[1]/div[5]/div[2]/ol/li/div/a/span/span/img").click()
    time.sleep(2)