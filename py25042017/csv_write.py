
osoba = ["pamela", "anderson", 50]

osoba_str = [str(dane) for dane in osoba]

dane_zapis = ",".join(osoba_str)

with open("osoby.txt", "a") as plik:
    plik.write(dane_zapis + "\n")