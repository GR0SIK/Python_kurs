# importujemy modul CSV

import csv

with open("osoby.txt") as plik:

    # tworzymy czytnik
    czytnik = csv.reader(plik)

    for line in czytnik:
        print(line)

dane = ["Bartosz", "Moje", "33"]
with open("osoby.txt", "a") as plik:
    # tworze zapisywacz
    zapisywacz = csv.writer(plik)
    # writerow zapisuje dane do CSV
    zapisywacz.writerow(dane)

