array = [1, 2, 3, 4]
for n in array:
    print(n)
array = [i for i in range(1, 10)]
print(array)

print("_______________")

x = 0
z = 0
array = [1, 2, 3, 4, 5]
for n in array:
    x = n + x
    z += 1
    print(n)
print(x)
print(int(x/z))


