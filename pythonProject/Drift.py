# inp = input("Введите размер массива\n")
# inp = int(inp)
# w = 0
# while w <= int(inp):
#     z = input("наполните массив\n")
#
#     mas = [int(z) for n in range(0, inp)]
#     w += 1
#
#
# z = 0
# for z in range(0, 101, 2):
#     z = z + z
#     print(z)
# print('Сумма всех четных от 0 до 100 включительно =', z)
#
#
# z = 'python'
# print(z[1:2])
#
# s = 'bfgshbkis'
#
# print(s[-2:2:-2])
#
#
# def f(z):
#     for y in xrange(2, z):
#         if z % y == 0: return 0
#     return 1
# print filter(f, xrange(2, 100))
#
# number = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
# def f(z):
#         if z < 50 and (z % 2) == 0 : return 0
#         else:
#              return 1
#
# h = filter(f, number)
# print(list(h))
#
# number = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
# def f(z):
#         if (z % 2) != 0 and z > 50 : return 1
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
#         z = 11
#         while z > 1:
#             z -= 1
#             print(f'Number: {z}')
#             time.sleep(self.interval)
#
#
# t = ClockThread(0.5)
# t.start()
# t.join()

# mylist = [z*z for z in range(3)]
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

if functools.reduce(lambda z, y : z and y, map(lambda p, q: p == q,l1,l2), True):
	print ("Списки l1 и l2 одинаковые")
else:
	print ("Списки l1 и l2 не одинаковые")

if functools.reduce(lambda z, y : z and y, map(lambda p, q: p == q,l1,l3), True):
	print ("Списки l1 и l3 одинаковые")
else:
	print ("Списки l1 и l3 не одинаковые")'''
#
# def translate():
#
#     dic = {'а': 'a', 'б': 'b', 'в': 'v'}
#     for key in dic:
#      yield key
#      f = lambda : [i for i in key]
#      print(f())
#
#
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



