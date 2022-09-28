
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
if num2 == 0:
    z = "бесконечность"
    print("z =", z)
else:
    z = num1 / num2
    print(num1, "/", num2, "=", int(z))
