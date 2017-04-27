# dane
monety =        [5, 2, 1, 0.5, 0.2, 0.1]
monety_reszta = [0, 0, 0,   0,   0,   0]

banknot = 20
zakup = 8.30
reszta = banknot - zakup

# indeks do trzymania pozycji listy
indeks_mon_reszta = 0

for moneta in monety:
    if reszta >= moneta:
        ilosc = reszta // moneta
        wartosc = ilosc * moneta
        reszta = round(reszta - wartosc, 1)

        #reszta = reszta - wartosc

        monety_reszta[indeks_mon_reszta] = ilosc

    indeks_mon_reszta += 1

print("Reszta do wydania:", monety_reszta)