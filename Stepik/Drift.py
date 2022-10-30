
later = input('Введите букву \n')
word = input('Введите слово \n')
x = 0
for q in word:
    if q == later:
        x += 1
print(x)