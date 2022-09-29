# inp = input("Введите размер массива\n")
# inp = int(inp)
# w = 0
# while w <= int(inp):
#     x = input("наполните массив\n")
#
#     mas = [int(x) for n in range(0, inp)]
#     w += 1
#
#
# z = 0
# for x in range(0, 101, 2):
#     z = x + z
#     print(x)
# print('Сумма всех четных от 0 до 100 включительно =', z)
#
#
# x = 'python'
# print(x[1:2])
#
# s = 'bfgshbkis'
#
# print(s[-2:2:-2])
#
#
# def f(x):
#     for y in xrange(2, x):
#         if x % y == 0: return 0
#     return 1
# print filter(f, xrange(2, 100))
#
# number = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
# def f(x):
#         if x < 50 and (x % 2) == 0 : return 0
#         else:
#              return 1
#
# h = filter(f, number)
# print(list(h))
#
# number = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
# def f(x):
#         if (x % 2) != 0 and x > 50 : return 1
#         else:
#              return 0
#
# h = filter(f, number)
# print(list(h))
#
#
# number = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
# for i in number:
#     if i > 50 and i % 2 != 0:
#
#        print(i)
#
#
#
#
# from random import uniform
# numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
# a = int(uniform(0, 13))
# print(numbers[a])
#
#
# from module import random as ran
# a = "123"
# ran(a)
#
#
# import threading
# import time
#
# class ClockThread(threading.Thread):
#     def __init__(self, interval):
#         super().__init__()
#         self.daemon = True
#         self.interval = interval
#
#     def run(self):
#         x = 11
#         while x > 1:
#             x -= 1
#             print(f'Number: {x}')
#             time.sleep(self.interval)
#
#
# t = ClockThread(0.5)
# t.start()
# t.join()

# mylist = [x*x for x in range(3)]
# print(mylist)
# for i in mylist:
#  print(i)


# def numbers_range(n):
#     for i in range(n):
#         yield i
#
# a = numbers_range(4)
# for b in a:
#     print(b)

# def word():
#     for a in 'world':
#      yield a
#
# z = 'world'
# # word(z)
# print(word())

# class transliteration():
#
#     def translate(self):
#         dic = {'а': 'a', 'б': 'b', 'в': 'v'}
#         for self.key in dic:
#          return self.key
#
#     def cycle(self):
#      for item in self.key:
#       print(item)


'''
import functools

l1 = [10, 20, 30, 40, 50]
l2 = [10, 20, 30, 50, 40, 70]
l3 = [10, 20, 30, 40, 50]

if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,l1,l2), True):
	print ("Списки l1 и l2 одинаковые")
else:
	print ("Списки l1 и l2 не одинаковые")

if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,l1,l3), True):
	print ("Списки l1 и l3 одинаковые")
else:
	print ("Списки l1 и l3 не одинаковые")'''

# def translate():
#
#     dic = {'а': 'a', 'б': 'b', 'в': 'v'}
#     for key in dic:
#      yield key
#      f = lambda : [i for i in key]
#      print(f())


# def benchmark(func):
#     import time
#
#     def wrapper(arg):
#         start = time.time()
#         func(arg)
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end - start))
#
#     return wrapper
#
#
# @benchmark
# def fetch_webpage(i):
#     import requests
#     webpage = requests.get('https://google.com')
#     w = str(webpage)
#     assert w[11:14] == i
#
# benchmark(fetch_webpage)('200')


# import unittest
# from selenium import webdriver
#
#
# class test_browser(unittest.TestCase):
#
#     def browser(self):
#         self.driver = webdriver.Chrome('chromedriver.exe')
#
#     def test_click(self):
#         self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject")
#         self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[1]').click()
#         assert 1 == 1
#
#     def hello(self):
#         print('hello')


# class Restaurant():
#
#     def __init__(self, restaurant_name, cuisine_type, grade):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.grade = grade
#
#     def describe_restaurant(self):
#         print('Name -', self.restaurant_name, '|','Kitchen -', self.cuisine_type)
#
#     def grade_restaurant(self):
#         if self.grade > 5 or self.grade <=0:
#             print ('grade -', '"Не корректный ввод"')
#         else:
#             print('grade -', self.grade)
#
#     def open_restaurant(self):
#         print('restaurant open!'.title())
#
# My_res = Restaurant('Moskow', 'Russian', 6)
# My_res.describe_restaurant()
# My_res.grade_restaurant()
# My_res.open_restaurant()
#
# My_res1 = Restaurant('Pushkin', 'Russian', 5)
# My_res2 = Restaurant('Sova', 'Russian', 3)
# My_res3 = Restaurant('Venesia', 'Italian', 4)
#
# My_res1.describe_restaurant()
# My_res2.describe_restaurant()
# My_res3.describe_restaurant()


'''
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import os
import time
from pprint import pprint

# тестовая страница, на которой мы ищем
target_page = "https://yandex.ru/"
# то самое выражение XPath, которое мы тестируем
xpath_testing = "//div[contains(@class, 'home-logo')]//child::*"

dir_current = os.getcwd()
driverLocation = dir_current + "\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = Chrome(driverLocation, chrome_options=chrome_options)
data_text = driver.get(target_page)
time.sleep(3)
try:
    elements_ = driver.find_elements(By.XPATH, xpath_testing)

    for element_ in elements_:
        pprint(f"Выбран элемент с тегом: \"{element_.tag_name}\"")
        pprint(f"Содержимое атрибута class: \"{element_.get_attribute('class')}\"")
        pprint(f"Текстовое содержимое элемента: {'Нет содержимого' if not element_.text else element_.text}")

except:
    print('Элемент по заданному XPath выражению не найден :(')

finally:
    driver.quit()'''

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://allure.x5.ru/')

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
batton_enterance = driver.find_element('xpath', '//*[@id="passp:sign-in"]')
batton_enterance2 = driver.find_element('xpath', '//*[@id="passp:sign-in"]')

login_username = driver.find_element('xpath', '//*[@id="root"]/div/div/div/div[2]/div/div/form/div[2]/div[1]/div/div/div[2]')

button_Bunk_Manager_Login = driver.find_element('html/body//div[2]/div/div[1]/div[2]/button')
input_name = driver.find_element('xpath', '//input[@type="text"]')
input_cod = driver.find_element('xpath', '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div[1]/div[2]/div/ul[1]/li[1]')

