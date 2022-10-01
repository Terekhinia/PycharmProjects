from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    browser.implicitly_wait(10)
    x_elem = browser.find_element(By.ID, 'treasure')
    x = x_elem.get_attribute('valuex')
    cod = abs(12*math.sin(int(x)))
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(cod)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    radiobuton = browser.find_element(By.ID, 'robotsRule')
    checkbox.click()
    radiobuton.click()
    # time.sleep(2)
    # browser.switch_to.alert.accept()
    buton_Submit = browser.find_element(By.CLASS_NAME, 'btn-default')
    buton_Submit.click()
finally:
    time.sleep(10)
    browser.quit()