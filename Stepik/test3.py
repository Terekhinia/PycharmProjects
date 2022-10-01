from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)
    browser.implicitly_wait(10)
    input1 = browser.find_element(By.CLASS_NAME, 'first')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CLASS_NAME, 'second')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'third')
    input3.send_keys("Mail@mail.ru")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

