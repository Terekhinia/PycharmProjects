
def getmax():
    mut = []
    i = 0
    while True:
        a = input("Введите число - ")
        if a == 'end':
            break
        mut.append(int(a))
    max = mut[0]
    for n in mut:
        if n > max:
            max = n
    print(mut)
    return max



def getmin():
    mut = []
    while True:
        a = input("Введите число - ")
        if a == 'end':
            break
        mut.append(int(a))
    min = mut[0]
    for n in mut:
        if n < min:
            min = n
    print(mut)
    return min


def getsum():
    mut = []
    while True:
        a = input("Введите число - ")
        if a == 'end':
            break
        mut.append(int(a))
    sum = int(0)
    for n in mut:
        sum += n
    print(mut)
    return sum




def changer_cortage(z, x, y):
    try:
        z = list(z)
        z[x] = y
        z = tuple(z)
        print(z)
    except IndexError:
        print('Данного индекса не существует; error:<IndexError>')
    except TypeError:
        print('Данная функция работает только со структурным типом данных; error:<TypeError>')