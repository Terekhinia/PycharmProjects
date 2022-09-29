# Функции для работы со списками и кортежами
'''
list = [1, 5, 3, 7]
list.index(1) # выводит номер элемента 1
list.append(9) # добавляет число 9 в конец списка
print(list)
 # заменяет индекс 0 на число 9
print(list)
list.extend([0, 9]) # добавляет к списку список [0, 9]
print(list)
list.remove(0) # удаляет число 0 из списка
print(list)
list.pop(0) # удаляет индекс 0
print(list)
rl = []
list2 = ['q', 'e', 'r']
rl.extend(list) # записывает в переменную rl значение списка list
rl.extend(list2) # добавляет в переменную rl к списку list список list2 одним списком (rl = [list, list2])
print(rl)
list.clear() # удалить список
print(list)
list.sort() # сортирует по возростанию
sor = sorted(list2) # сортирует по алфавиту и записывает в переменную sor
print(list)
list.sort(reverse=True) # сортировать по убыванию
print(list)

Пример применения функции sort с использованием key:
children = ['arbuzov_2000', 'petrov_1999', 'ivanov_2001']
def by_year(name):
    year = name.split('_')[-1]
    return year

print(by_year(children[0]))

s_children = sorted(children, key=by_year)
print(s_children)

>>2000
>>['petrov_1999', 'arbuzov_2000', 'ivanov_2001'] # отсортировалось по дате рождения

'''

# Функции для работы с множествами
'''
set = {1, 3, 2, 2, 10}
print(set)
set.sort(reverse=True) # у множества нельзя менять порядок
print(set)
set.remove(3) # удаляет элемент 3, если этого эл. не будет выдаст ошибку
print(set)
set.discard(5) # удаляет элемент 5, если этого эл. не будет ошибку не выдает
print(set)
set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 5}
print(set1.union(set2)) # соединяет два множества
print(set1.intersection(set2)) # выводит общие значения
print(set1.difference(set2)) # противоположная функция
set1.clear()
set2.clear()
print(set1, set2)
print("______________")
'''

# Функции для работы со словарями
'''
d = {'name': 'Ivan', 'age': 35}
print(d)
d.setdefault('IsWorking', True) # функция добавления параметра в словарь
print(d)
print(d.get('age')) # выводит значение по ключу
d.pop('name') # удаляет значение по ключу
print(d)
print(d.keys()) # выводит все ключи словаря
keys = list(d.keys())
print(keys)
print(keys[0])
print(d.values()) # выводит все значения словаря
print(d.values[0]) # выводит значение по индексу ключа
d['age'] = 40 # замена значения по ключу
d['isMale'] = True # добавление ключа и значения
print(d)
new = {'name': 'dima', 'tel': '123'}
d.update(new) # добавляет значения из другого словаря или заменяет значение если ключи совпажают
d.update(name='dima', tel='123') # альтернативная запись
print(d)
tel= d.get('tel') # выводит None если в словаре отсутствует запрашиваемый ключ
print(tel)
tel = d.get('tel', '123') # выводит '123' если в словаре отсутствует запрашиваемый ключ
print(tel)
d.setdefault('tel', '123') # добавляет в словарь ключ 'tel' со значением'123' если в словаре отсутствует запрашиваемый ключ
print(d)
q = d.items() # расспаковка словаря на картежи 
print(q)
>>dict_items([('name', 'Ivan'), ('age', 30), ('tel', '123')])
d.clear() # очистка словаря
print(d)
'''

# Функции для работы со строками
'''
a = '   hello world'
len(a) # возвращает длинну строки
a.upper() # приводит строку к верхнему регистру
a.title() # каждое отдельное слово начинается с заглавной буквы
a.strip() # очищает строку от пробелов
# или от любых других символов которые будут указаны в качестве аргумента (прим. strip(;) - удалит все ';')
a.isdigit() # возвращает True если все эллементы строки являются цыфрами 
a.split() # создаст из строки список ['hello', 'world'], разделение будет по пробелу, можно задать разделение по любому символу
a.join() # обратная функция split
a.startswith('a') # возвращает True если строка начинается на 'a'
'''

# Функции для работы с файлами
'''
faile1 = open('a.txt', 'w') # открыть фаил, w-перезаписывает(удаляя предыдущие записи), а-дозаписывает
faile1.write("abc 123\n890")
faile1.close()
faile1 = open('a.txt', 'r') # открыть фаил, r-чтение
print(faile1.read()) # вывести все содержимое файла
faile1.seek(0) # обнулить вывод (а то дальше ничего не выведет)
print(faile1.read(2)) # вывести первые два знака
faile1.seek(0)

for l in faile1:
    print(l)    # пример как вывести построчно

faile1 = open('C:\\Users\\user\\Desktop\\123.txt', 'w')
faile1.write("hello")
faile1 = open('C:\\Users\\user\\Desktop\\123.txt', 'r')
print(faile1.read())
print("______________________")
'''

# Функции для работы с датой и временем
'''
from datetime import *
from time import *
print(date.today())
print(datetime.today())
d = date(2021, 12, 15)
print(d)
dt = datetime(2021, 12, 15, 23, 7, 30)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.minute)
print(dt.second)
print(dt.strftime("%Y.%m.%d %H:%M:%S")) # позволяет формировать вывод даты в любом варианте
print(time()) # выводит количество секунд с 01.01.1970г. 00:00
dt = datetime.fromtimestamp(3684954454) # переводит секунды в дату
print(dt)
print(dt.timestamp()) # выводит сколько секунд до даты (от 01.01.1970) вложенной в объект dt

'''



# Подстановка переменных в строку (Don't Repeat Yourself)
'''
name = 'Leon'
number = 100

# pattern = 'Hello {} - {}'
# result = pattern.format(name, number) # подставляет значения name и number в {} строки

# pattern = '{movie} - {number}' # подстановка через ключ
# result = pattern.format(movie=name, number=100)

result = f'{name} - {number}'
print(result) 
'''


