# odzielne listy

def dodaj_imie(imie, imiona=None):
    ''' oczekuje str'''
# sprawdza czy lista jest na wartosc nic, i wtedy dopiero otrzymuje odzielne obiekty
    if imiona is None:
        imiona = []
    imiona.append(imie)
    return imiona

lista_imion = dodaj_imie("Ola")
print(lista_imion)

lista_imion2 = dodaj_imie("Ala")
print(lista_imion2)

lista_imion3 = dodaj_imie("Piotrek")
print(lista_imion3)

# aby dodac do istniejacej listy musimy wskazac liste
dodaj_imie("Mariola", lista_imion2)
print(lista_imion2)

