import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://magento.softwaretestingboard.com"
global browser

def test_add_to_cart():
    Popup = browser.find_element(By.CLASS_NAME, "fc-button-label")
    Popup.click()
    Select_Clothes_Image = browser.find_element(By.XPATH, "//div[contains(@class, 'products-grid')]/ol/li/div/a/span/span/img")
    Select_Clothes_Image.location_once_scrolled_into_view
    Select_Clothes_Image.click()
    Select_Clothes_Size = browser.find_element(By.ID, "option-label-size-143-item-168")
    Select_Clothes_Size.click()
    Select_Clothes_Color = browser.find_element(By.ID, "option-label-color-93-item-57")
    browser.execute_script('arguments[0].scrollIntoView(true)', Select_Clothes_Color)
    Select_Clothes_Color.click()
    Add_To_Cart = browser.find_element(By.ID, "product-addtocart-button")
    Add_To_Cart.click()
    browser.implicitly_wait(10)
    time.sleep(2)
    Cart_Page = browser.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/a")
    browser.execute_script('arguments[0].scrollIntoView(true)', Cart_Page)
    Cart_Page.click()


def test_delete_from_cart():
    Popup = browser.find_element(By.CLASS_NAME, "fc-button-label")
    Popup.click()
    Select_Clothes_Image = browser.find_element(By.XPATH,"//div[contains(@class, 'products-grid')]/ol/li/div/a/span/span/img")
    Select_Clothes_Image.location_once_scrolled_into_view
    Select_Clothes_Image.click()
    Select_Clothes_Size = browser.find_element(By.ID, "option-label-size-143-item-168")
    Select_Clothes_Size.click()
    Select_Clothes_Color = browser.find_element(By.ID, "option-label-color-93-item-57")
    browser.execute_script('arguments[0].scrollIntoView(true)', Select_Clothes_Color)
    Select_Clothes_Color.click()
    Add_To_Cart = browser.find_element(By.ID, "product-addtocart-button")
    Add_To_Cart.click()
    browser.implicitly_wait(10)
    time.sleep(2)
    Cart_Page = browser.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/a")
    browser.execute_script('arguments[0].scrollIntoView(true)', Cart_Page)
    Cart_Page.click()
    Delete_Clothes = browser.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/div/div/div/div[2]/div[4]/ol/li/div/div/div[3]/div[2]/a")
    Delete_Clothes.click()

def test_change_quantity():
    Popup = browser.find_element(By.CLASS_NAME, "fc-button-label")
    Popup.click()
    Select_Clothes_Image = browser.find_element(By.XPATH,"//div[contains(@class, 'products-grid')]/ol/li/div/a/span/span/img")
    Select_Clothes_Image.location_once_scrolled_into_view
    Select_Clothes_Image.click()
    Select_Clothes_Size = browser.find_element(By.ID, "option-label-size-143-item-168")
    Select_Clothes_Size.click()
    Select_Clothes_Color = browser.find_element(By.ID, "option-label-color-93-item-57")
    browser.execute_script('arguments[0].scrollIntoView(true)', Select_Clothes_Color)
    Select_Clothes_Color.click()
    Add_To_Cart = browser.find_element(By.ID, "product-addtocart-button")
    Add_To_Cart.click()
    browser.implicitly_wait(10)
    time.sleep(2)
    Cart_Page = browser.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/a")
    browser.execute_script('arguments[0].scrollIntoView(true)', Cart_Page)
    Cart_Page.click()
    Quantity = browser.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/div/div/div/div[2]/div[4]/ol/li/div/div/div[2]/div[2]/input")
    Quantity.click()
    Quantity.clear()
    Quantity.send_keys("3")

@pytest.fixture(autouse=True)
def run_around_tests():
    global browser
    browser = webdriver.Chrome()
    browser.get(link)
    yield
    browser.quit()