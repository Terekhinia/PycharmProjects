# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# def test_function():
#
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(1)
#     driver.get('https://allure.x5.ru/project/123/dashboards')
#     Username_input = driver.find_element('name', 'username')
#     Username_input.send_keys('Ivan.Terekhin')
#     Password_input = driver.find_element('name', 'password')
#     Password_input.send_keys('MannX504')
#     Button_Continue = driver.find_element('xpath', '//button[@type="submit"]')
#     Button_Continue.click()
#     # Button_Allprojects = driver.find_element('xpath', '//span[text()="All projects"]')
#     # Button_Allprojects.click()
#     Project = driver.find_elements('css selector', 'div.ProjectRow__name a')
#     Project_names = [element.text for element in Project]
#     assert 'СЭД' in Project_names
#     Button_target = driver.find_element('xpath', '//*[@class="SideMenu__nav-item"]')
#     ActionChains(driver).move_to_element(Button_target).perform()
#     driver.quit()
#



