liczba = input("Podaj liczbe: ")
podzielnik = input("Podaj podzielnik: ")

# int(liczba) - zamiana string na intyger

if liczba.isdigit() and podzielnik.isdigit():
    if int(liczba) % int(podzielnik) == 0:
        print(" Liczba jest podzielna przez ", podzielnik)
    else:
        print("Liczba nie jest podzielna przez", podzielnik)
        print("Wynik dzielenia:", int(liczba) / int(podzielnik))
else:
    print("Podaj liczbę !!!")
