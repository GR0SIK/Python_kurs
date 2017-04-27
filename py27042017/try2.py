try:

    with open("dane.txt") as plik:
        print(plik.read())
except FileNotFoundError as e:
    print(e.args)
    print("Podany plik nie istnieje !!!")

    raise ValueError("Komunikat mój o błedzie")
except Exception:
    print("Pojawił się błąd !!!!")

print("Dalej cześć programu")
