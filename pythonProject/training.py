# def pos_add(a, b):
#       return abs(a + b) # abs - возвращает целочисленное значение
#
# print(pos_add(-5, 3))

# def num_sum(a):
#     if isinstance(a, int): # Похожа на функцию type(), проверяет принадлежность а к типу int
#         a_to_str = str(abs(a))
#         s = 0
#         for i in a_to_str:
#             s += int(i)
#         return s
#     return 'Это не целое число'
#
# print(num_sum(-146))
# print(num_sum(-11))
# print(num_sum(2.5452))

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
#
#     def make_sound(self):
#         print("Meow")
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
#
#     def make_sound(self):
#         print("Bark")
#
#
# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)
#
# for animal in (cat1, dog1):
#     animal.info()
#     animal.make_sound()


# a = int(input('Введите число: '))
# cond = a == 1 or a == 2 or a == 3
#
# if cond:  # если cond == True
#     x = 0
# else:
#     x = 3
# print(x)
# # тоже самое с помощью конструктора
# x = 0 if cond else 3
# print(x)

# A = [1] * 9
# A.insert(0, 9)
#
# print(A, '\n', len(A), ';', A[0], '\n', A[-3:-1], sep='')
#
#
# myset = {'name'}

# for i in range(3, 5):
#     print(i)
#
# z = (1, 2, 3)
# z = list(z)
# z[0] = 2
# z = tuple(z)
# print(z)
# A = {1, 2, 3}
# B = {4, 5, 6}
# x = a.intersection(z)
# print(A.difference(B))



import pytest
from selenium import webdriver
driver = webdriver.Chrome('../pythonProject/chromedriver.exe')


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located)
