mas = ['привет', 'пока', 'досвидания']
i = 0
while True:
    while i < len(mas):
        print(i, "-", mas[i])
        i += 1
    x = input("Введите индекс элемента который хотите посмотреть ")
    x = int(x)
    if x < 0 or x >= len(mas):
      print("нах пошел")
    else:
      print(mas[x])
      break
