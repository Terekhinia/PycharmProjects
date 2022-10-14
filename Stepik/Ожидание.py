from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pyperclip


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
try:
    button_Book = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button_Book.click()
    button_Submit = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_Submit)
    x_elem = browser.find_element(By.ID, 'input_value')
    x = x_elem.text
    cod = str(math.log(abs(12*math.sin(int(x)))))
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(cod)
    button_Submit.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    browser.switch_to.alert.accept()

finally:
    time.sleep(5)
    browser.quit()