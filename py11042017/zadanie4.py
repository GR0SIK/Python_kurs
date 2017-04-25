liczba = input("Podaj liczbe: ")
podzielnik = input("Podaj podzielnik: ")


if liczba.isdigit() and podzielnik.isdigit():

    wynik = int(liczba) / int(podzielnik)

    if float(round(wynik, 2)).is_integer():
    #if round(wynik, 2).:
        print("Liczba {} jest podzielna przez {}".format(liczba, podzielnik))
    else:
        print("Liczba {} nie jest podzielna {}".format(liczba, podzielnik))
        print("Wynik dzielenia: {:.2f}".format(wynik))



