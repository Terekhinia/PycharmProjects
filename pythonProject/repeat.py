
"""
i = 0
while i < 10:
    i += 1
    print(i, "Hello")
"""
#8
"""
a = str(0)
z = int(0)
while True:
      z = int(a) + z
      a = input("Введите число ")
      if a == "=":
         print("Сумма = ", z)
         a = 0
         continue
      if a == "exit" or a == "quit":
         break
print("Конец")
"""

#9
"""list = ['h', 'e', 'l', 'l', 'o']
i = 0
while i < len(list):
    print(i + 1, '-', list[i])
    i += 1
inp = int(input("Введите индекс \n"))
if inp > len(list) or inp < 0:
    print("Элемента с таким индексом не существует")
else:
    print(list[inp-1])
"""
#10
"""array = [1, 5, 7, 10, 2]
z = 0
z = 0
for n in array:
    z += 1
    z = n + z
print(z)
print(int(z/z))


z = 0
z = 0
arr = [i for i in range(1, 10)]
for n in arr:
    z += 1
    z = n + z
print(z)
print(int(z/z))
"""

#11

"""
import random

inp = int(input("Введите количество элементов списка: "))
arr = [int(random.random() * 10) for i in range(0, inp)]
print(arr)
n = 0
while n < len(arr):
    print(arr[n])
    n += 1
myset = set(arr)
print(myset)
z = 0
for z in myset:
    z = z + z
    print(z)
print("Сумма =", z)
myset = list(set(arr))
print(myset)
"""
#12
"""
inp = input("Введите произвольную строку: ")
mytuple = tuple(inp)
for z in mytuple:
    print(z)"""

#13
"""
mydict = dict()
inpname = input("Введите свое имя: ")
inpage = input("Введите свой возраст: ")
mydict = {"Name": inpname, "Age": inpage}
for key in mydict:
    print(key, '=', mydict[key])"""

#14
'''
n = int(input('Введите число: '))
def funk(n):
    if n % 2 == 0:
        n = True
    else: n = False
    return n
print(funk(n))'''


"""def lst(*arr):
    max = int()
    for z in arr:
        if z > max:
            max = z
    return max
print(lst(0, 10, 2, 13))"""

'''def bigsum(*num):
    z = 0
    z = 0
    for n in num:
        z += 1
        z += n
    return z/z
print(bigsum(1, 5, 6))'''

#15


#16
'''
import mymodule as my
my.getsum
print(my.getsum())'''

#17
"""
z = int(input('Введите число - '))
try:
    print(z/0)
except ZeroDivisionError:
    print('Бесконечность')"""

"""
import subprocess
import io

sp = subprocess.Popen(['TIME'], stdout=subprocess.PIPE, shell=True)
print(sp)
out = io.TextIOWrapper(sp.stdout, encoding="cp866")
s = ' '
while s:
    s = out.readline()
    print(s)"""
