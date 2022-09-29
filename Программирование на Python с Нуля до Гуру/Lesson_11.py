import random
arr = int(random.random() * 100)
print(arr)
print("_______________")


i = 0
inp = input("Введите количество элементов для списка: ")
inp = int(inp)
mas = [int(random.random() * 10) for n in range(0, inp)]
while i < len(mas):
    print(mas[i])
    i += 1
newset = set(mas)
print(mas)
q = len(newset)
z = [n for n in newset]
print(z)
