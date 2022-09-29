num = str()
while num != "exit":
   x = 0
   num = 0
   while True:
       x = int(num) + int(x)
       num = input("Введите число для cуммирования:")
       if num == "":
           num = 0
       if num == "sum":
           print(x)
           break
       if num == "exit":
           break






