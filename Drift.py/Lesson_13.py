mydict = dict()
print(mydict)
mydict = {'Name' : 'Без имени', 'Age' : -1}
z = input("Введите свое имя\n")
x = input("Введите свой возраст\n")
mydict = {'Name' : z, 'Age' : x}
for key in mydict:
    print(key, "=", mydict[key])


