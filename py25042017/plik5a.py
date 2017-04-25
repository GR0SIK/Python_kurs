# dzieki takiemu zapisowi nie musimy pamietac o zamknieciu pliku txt
with open("mojplik.txt", "r") as plik:
    # blok kodu, pamiętam o zagłębieniu
    print(plik.read())

print("Nie musze pamietac o zamknieciu")