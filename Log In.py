from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import numpy as np

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    Button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    Button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    inputValue = browser.find_element(By.ID, "input_value")
    inputValueNumber = int(inputValue.text)
    result = np.log(np.abs(12*np.sin(inputValueNumber)))
    answerField = browser.find_element(By.ID, "answer")
    answerField.send_keys(result)
    submitButton = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submitButton.click()

finally:
    time.sleep(30)
    browser.quit()