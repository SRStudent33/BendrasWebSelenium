from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium. webdriver.support.select import Select
import time

link="https://magento.softwaretestingboard.com/"

browser = webdriver.Chrome()
browser.get(link)

captcha = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/button[1]/p")
captcha.click()

time.sleep(3)

account = browser.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[3]/a")
account.click()

time.sleep(3)

name = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[1]/div[1]/div/input")
name.send_keys("Edvinas")

time.sleep(3)

surname = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[1]/div[2]/div/input")
surname.send_keys("Gaidamavicius")

time.sleep(3)

email = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[1]/div/input")
email.send_keys("edvinas2003@gmail.com")

time.sleep(3)

password = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[2]/div/input")
password.send_keys("edvinas2003!")

time.sleep(3)

confirm_password = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[3]/div/input")
confirm_password.send_keys("edvinas2003!")

time.sleep(3)

submit = browser.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/div/div[1]/button")
submit.click()

time.sleep(3)
