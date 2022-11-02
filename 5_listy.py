programowanie=['Python', 'PHP', 'C#', 'JS', 'Java']
print(programowanie)
print(type(programowanie))
first=programowanie[0]
print("Pierwszy element: ", first)

threeElements=programowanie[0:3]
print("Trzy elementy: ", threeElements)

lastElements=programowanie[-1]
print("Ostatni element: ", lastElements)

#dodanie nowego elementu na koniec listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

#zliczanie elementu w liście
countElements=programowanie.count('Python')
print(countElements)

#zliczanie elementów w liście
countElementsOfList=len(programowanie)
print(type(countElementsOfList))
print('Ilość elementów w liście: ' + str(countElementsOfList))

#połączenie list
anotherList=['C', 'C++']
programowanie.extend(anotherList)
print('Lista programowanie: ' + str(programowanie))
print('Lista anotherList: ' + str(anotherList))

#usuwanie elementów z listy
new=programowanie
print('New list: ' + str(new))
new.clear()
print('New list: ' + str(new))
print('Rozmiar New list: ' + str(len(new)))

print('Programowanie: ' + str(programowanie))
print('Rozmiar listy programowanie: ' + str(len(programowanie)))

x=8
print(x)
y=x
print(y)

y=5
print(x)
print(y)

'''
Dodaj listę o nazwie: country
Przypisz do niej 5 elementów
Poproś użytkownika, aby dodał dwa nowe elementy do listy
Uzytkownikowi wyświetl listę do wyboru:
1) Wyświetl pierwsze 3 elementy listy
2) Wyświetl elementy listy, które dodałem (dane pobierz z listy)
3) Wyświetl zawartość listy
4) Wyczyść zawartość listy
5) Znajdź element w liście, który poda użytkownik (wyświetl czy jest dodany do listy)
Użytkownik raz dokonuje wyboru z listy.
Wyświetl zawartość listy po wykonaniu operacji przez użytkownika.
'''
print('-----')
country=['Polska', 'Brazylia', 'Holandia', 'Anglia', 'Czechy']
element1 = input("Podaj pierwszy kraj jaki chcesz dodać: ")
element2 = input("Podaj drugi kraj jaki chcesz dodać: ")
country.append(element1)
country.append(element2)

print('***MENU***')
print('1) Wyświetl pierwsze 3 elementy listy')
print('2) Wyświetl elementy listy, które dodałem (dane pobierz z listy)')
print('3) Wyświetl zawartość listy')
print('4) Wyczyść zawartość listy')
print('5) Znajdź element w liście, który poda użytkownik')

choice = int(input("Mój wybór: "))

if choice == 1:
    print('Pierwsze trzy elementy listy: ', country[0:3])
elif choice == 2:
    print('Elementy z listy które zostały dodane: ', country[-2])
else choice == 3:
    print('Zawartość listy: ')
