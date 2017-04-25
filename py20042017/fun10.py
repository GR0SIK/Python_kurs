# doaje do tej samej listy

def dodaj_imie(imie, imiona=[]):
    imiona.append(imie)
    return imiona

lista_imion = dodaj_imie("Ola")
print(lista_imion)

lista_imion2 = dodaj_imie("Ala")
print(lista_imion2)

lista_imion3 = dodaj_imie("Piotrek")
print(lista_imion3)