from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_function():

    #Навигация
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://allure.x5.ru/project/123/dashboards')
    Username_input = driver.find_element('name', 'username')
    Username_input.send_keys('Ivan.Terekhin')
    Password_input = driver.find_element('name', 'password')
    Password_input.send_keys('MannX504')
    Button_Continue = driver.find_element('xpath', '//button[@type="submit"]')
    Button_Continue.click()
    time.sleep(2)
    Batton_Test_case = driver.find_element('xpath', '//*[@name="test-cases-icon"]')
    Batton_Test_case.click()
    Page_Test_case = driver.find_element('xpath', '//*[@class="list SideMenu__list"]/li[4]/a')
    Page_Test_case_url = Page_Test_case.get_attribute('href')
    assert 'test-cases' in Page_Test_case_url
    driver.back()
    driver.back()
    driver.back()
    Title_url = driver.current_url
    assert 'https://allure.x5.ru/' in Title_url
    #Проверка тест-кейсов Структура
    Batton_Test_case = driver.find_element('xpath', '//*[@name="test-cases-icon"]')
    Batton_Test_case.click()

test_function()