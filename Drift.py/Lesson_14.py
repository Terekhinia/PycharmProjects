
'''
def funk(x):
    if x % 2 == 0:
        x = True
    else:
        x = False
    return x

x = input('Введите переменную\n')
x = int(x)
print(funk(x))
'''

def getmax(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max

print(getmax([5, 7, 9, 52, 6]))


def bigsum(*num):
    x = 0
    z = 0
    for n in num:
        x += 1
        z += n
    return z / x



print(bigsum(1, 2 ,5 ,3))
