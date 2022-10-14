from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import pyperclip

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
browser.implicitly_wait(10)
try:
    input0 = browser.find_element(By.CLASS_NAME, 'btn')
    input0.click()
    browser.switch_to.alert.accept()
    x_elem = browser.find_element(By.ID, 'input_value')
    x = x_elem.text
    cod = math.log(abs(12*math.sin(int(x))))
    cod  = str(cod)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(cod)
    buton_Submit = browser.find_element(By.CLASS_NAME, 'btn')
    buton_Submit.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    browser.switch_to.alert.accept()

finally:
    time.sleep(10)
    browser.quit()