
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Search(unittest.TestCase):

     def setUp(self):
         self.drv = webdriver.Chrome('chromedriver.exe')

     def test_search(self):
         self.drv.get('https://Google.ru')
         assert 'Google' in self.drv.title # проверка что 'Google' присутствует в заголовке сайта
         elm = self.drv.find_element_by_name('q') # находим поле ввода браузера по значению name
         elm.send_keys('selenide') # ввести 'selenide' в поле ввода
         elm.send_keys(Keys.ENTER) # нажать ENTER
         pages = self.drv.find_element_by_xpath('//*[@id="rso"]//a')
         # находим первую ссылку на страницу
         page = pages.get_attribute('href')
         assert 'selenide.org' in page # проверяем что первая ссылка ведет на сайт selenide.org
         self.drv.find_element_by_link_text('Картинки').click() # нажать на кнопку Картинки
         img = self.drv.find_elements_by_class_name('VFACy') # список элементов
         img_link = img[0].get_attribute('href') # получение значение из выбранного атрибута "нулевого" эллемента
         assert 'selenide.org' in img_link # проверка значения атрибута с заданным параметром
         self.drv.find_element_by_link_text('Все').click() # нажать на кнопку Все
         pages1 = self.drv.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a')
         page1 = pages1.get_attribute('href')
         assert page == page1

     def tearDown(self):
         self.drv.close()

if __name__ == '__main__':
    unittest.main()
