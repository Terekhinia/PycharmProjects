"""""
inp = input("Введите размер массива\n")
inp = int(inp)
w = 0
while w <= int(inp):
    x = input("наполните массив\n")

    mas = [int(x) for n in range(0, inp)]
    w += 1


z = 0
for x in range(0, 101, 2):
    z = x + z
    print(x)
print('Сумма всех четных от 0 до 100 включительно =', z)
"""

"""x = 'python'
print(x[1:2])

s = 'bfgshbkis'

print(s[-2:2:-2])"""


"""def f(x):
    for y in xrange(2, x):
        if x % y == 0: return 0
    return 1
print filter(f, xrange(2, 100))"""

"""number = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
def f(x):
        if x < 50 and (x % 2) == 0 : return 0
        else:
             return 1

h = filter(f, number)
print(list(h))"""

"""number = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
def f(x):
        if (x % 2) != 0 and x > 50 : return 1
        else:
             return 0

h = filter(f, number)
print(list(h))
"""

"""number = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
for i in number:
    if i > 50 and i % 2 != 0:

       print(i)
"""


""""""""

"""from random import uniform
numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
a = int(uniform(0, 13))
print(numbers[a])
"""

"""from module import random as ran
a = "123"
ran(a)
"""

import threading
import time

class ClockThread(threading.Thread):
    def __init__(self, interval):
        super().__init__()
        self.daemon = True
        self.interval = interval

    def run(self):
        x = 11
        while x > 1:
            x -= 1
            print(f'Number: {x}')
            time.sleep(self.interval)


t = ClockThread(0.5)
t.start()
t.join()