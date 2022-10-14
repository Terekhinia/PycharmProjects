from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)
browser.implicitly_wait(10)
try:
    num_elem1 = browser.find_element(By.ID, 'num1')
    num_elem2 = browser.find_element(By.ID, 'num2')
    num1 = int(num_elem1.text)
    num2 = int(num_elem2.text)
    sum = num1 + num2
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    time.sleep(1)
    alert_text = browser.switch_to.alert.text


finally:
    time.sleep(5)
    browser.quit()