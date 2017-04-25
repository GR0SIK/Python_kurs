
# opis_kolum = None
baza = []

with open("osoby.txt") as plik:

    # print(plik.read())
    # print(plik.readlines())
    # lista kolum
    opis_kolum = plik.readline()

    for line in plik:
        # usuwamy whitespace
        line = line.strip()

        osoba = line.split(",")
        # print(osoba)

        baza.append(osoba)

print(baza)

for wpis in baza:
    print(wpis[0])