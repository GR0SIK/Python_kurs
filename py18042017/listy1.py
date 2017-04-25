# listy
# deklarowanie listy

lista = ["trzy", "jeden"]
lista1 = [2, 3, 4, 9, 0 ,3, 4]

print(lista)
print(lista1)

print(type(lista1))

lista2 = list("kwiatek")
print(lista2)

# aby połączyć rozbitą listę
el_string = ''.join(lista2)
print(el_string)

print(type(el_string))

lista3 = [1, "dwa", 3.0, range(3), [0, 1]]
print(lista3)
# len sprawdzanie długości
print(len(lista3))

# indeksowanie listy
print(lista3[2])
print(lista3[4][0])

#imie = "Ala"
#imie[0] = "o"
#
#print(imie)

lista3[1] = "osiem"
print(lista3)
