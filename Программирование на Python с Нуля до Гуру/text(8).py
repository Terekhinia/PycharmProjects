"""f = readme('123.txt', 'w')
f.write('Heiio!')
f = readme('123.txt', 'r')
print(f.read())
"""

"""with readme('123.txt', 'w') as f:
    str_list = ['Hello \n','World!']
    f.writelines(str_list)

with readme('123.txt', 'r') as f:
     print(f.read())
"""

with readme('C:\\Users\\user\\Desktop\\123.txt', 'r') as f:
     s = readme('123.txt', 'w')
     s.write(f.read()[::-1])


f = readme('C:\\Users\\user\\Desktop\\123.txt', 'r')
s = readme('123.txt', 'r')
print(f.read(), s.read())
