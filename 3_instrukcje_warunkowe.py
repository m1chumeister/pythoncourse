x=input('Podaj wartość: ')
if x=='10':
    print('Podałeś 10')
    print('xzc')
else:
    print('Inna wartość niż 10')
    print(type(x))

y=False
if y:
    print('prawda')
else:
    print('fałsz')

'''
Użytkownik podaje wartości trzech zmiennych x,y,z.
Wyświetl, która z tych trzech wartości jest największa.
Wykorzystaj instrkuje warunkową.
'''

x=input('Podaj x: ')
y=input('Podaj y: ')
z=input('Podaj z: ')

if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
else:
    print(z)
