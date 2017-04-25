# czy liczba jest podzielna przez 3, 5, lub 7
# input
# sprawdz czy to cyfry
liczba = input("Podaj liczbe: ")

if liczba.isdigit():
    if int(liczba) % 3 == 0:
        print(" Liczba jest podzielna przez 3")

    elif int(liczba) % 5 == 0:
        print("Liczba podzielna przez5")
    elif int(liczba) % 7 == 0:
        print("Liczba podzielna przez 7")

# jesli podzielna 3
    # napisz ze podzielna przez 3
# w prz. razie czy podzielna przez 5
    # napisz podzelna przez 5

else:
    print("Podaj liczbę !!!")