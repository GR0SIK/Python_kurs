try:

    with open("dane.txt") as plik:
        print(plik.read())
except FileNotFoundError as e:
    print(e.args)
    print("Podany plik nie istnieje !!!")
except Exception:
    print("Pojawił się błąd !!!!")

print("Dalej cześć programu")

