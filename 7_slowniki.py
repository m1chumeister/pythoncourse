slownik = {'klucz1' : 'wartosc1', 'klucz2' : 'wartosc2'}
print(slownik)
print(slownik['klucz1'])

'''
utwórz słownik o nazwie worker zawierający klucz: imie, nazwisko, miasto, wiek, imiona_dzieci, imiona_rodzicow
'''

worker = {
    'name' : 'Majkel',
    'surname' : 'Cherry',
    'city' : 'Poznań',
    'age' : 22,
    'childsNames' : ['Laura', 'Tymek'],
    'parentsNames' : ['Anna', 'Tomasz'],
    }

print(worker)
print(worker['childsNames'])
print(worker['childsNames'][0])

worker['height'] = 180
print(worker)

key = 'name'

if key in worker:
    del worker[key]
    print(f'klucz {key} został usunięty!')
else:
    print(f'klucz {key} nie został usunięty!')

print(worker)

'''
utwórz program totolotek, użytkownik podaje 6 liczb
'''
