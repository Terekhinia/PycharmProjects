"""f = open('123.txt', 'w')
f.write('Heiio!')
f = open('123.txt', 'r')
print(f.read())
"""

"""with open('123.txt', 'w') as f:
    str_list = ['Hello \n','World!']
    f.writelines(str_list)

with open('123.txt', 'r') as f:
     print(f.read())
"""

with open('C:\\Users\\user\\Desktop\\123.txt', 'r') as f:
     s = open('123.txt', 'w')
     s.write(f.read()[::-1])


f = open('C:\\Users\\user\\Desktop\\123.txt', 'r')
s = open('123.txt', 'r')
print(f.read(), s.read())
