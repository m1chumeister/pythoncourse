# try except
def div(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print('Nie wolno dzielić przez zero')

print(div(3, 10))
print(div(3, 0))

while True:
    try:
        num = int(input('Podaj liczbę całkowitą: '))
        print(f'Podałeś z klawiatury: {num}')
        break
    except ValueError:
        print('Podana wartość nie jest liczbą całkowitą')
