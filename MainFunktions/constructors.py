import time

password = '123'
user_input = ''

print('Welcom') if user_input else print('Wrong password')
#аналргично записи:
if user_input:
    print('Welcom')
else:
    print('Wrong password')


#Генератор списка от 0 до 10:
arr = [i for i in range(0, 10)]

# Выводит время выполнения команды
from time import *
start = time()
i = 0
while i < 1000000:
    i += 1
print("Время выполнения цикла: ", time() - start, "сек.")

# Расспаковка словаря через цикл for:
d = {'name': 'Ivan', 'age': 30, 'tel': '123'}
for key, values in d.items():
    print(key, values)


# Функция которая записывает заданный текст в текстовый файл 'readme' через print():
def print_wrapper(text):
    with open('readme', 'a') as f:
        print(text, file=f)

print_wrapper('kek')

# Пример работы функции lambda:
f = lambda x, y: x * y
print(f(5, 2))


# Построчный вывод значений из словаря
def return_values(dic):

    def value():
        for key in dic:
            yield dic[key]

    def cycle():
        for item in value():
            print(item)

    return cycle()

# Подстановка переменных в строку (Don't Repeat Yourself)

name = 'Leon'
number = 100

# pattern = 'Hello {} - {}'
# result = pattern.format(name, number) # подставляет значения name и number в {} строки

# pattern = '{movie} - {number}' # подстановка через ключ
# result = pattern.format(movie=name, number=100)

result = f'{name} - {number}'
print(result)

# Работа с исключениями
f = open('1.txt')
ints = []
try:
    for line in f:
         ints.append(int(line))
except ValueError:
    print('Это не число. Выходим.')
except Exception:
    print('Это что ещё такое?')
else:
    print('Всё хорошо.')
finally:
    f.close()
    print('Я закрыл файл.')

# Конструкция с перебором и изменением вывода списка
numbs = [1, 2, 3, 4, 5]
result = [x * x for x in numbs if x > 3]
print(result)

# Получение списком значений из xpath
for element in driver.find_elements_by_xpath
print(element.text)
print(element.tag_name)
print(element.parent)
print(element.location)
print(element.size)


# Скрипт явного ожидания
i = 0
while (i < 30):
    i += 1
    try:
        driver.find_element('name', 'first_name')
        break
    except NoSuchElementExeption:
        time.sleep(1)


