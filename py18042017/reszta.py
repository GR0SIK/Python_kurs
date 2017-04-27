# podaj ilosc wydanych monet

monety = [5, 2, 1, 0.5, 0.2, 0.1]

wydac = [0, 0, 0, 0, 0, 0]

banknot = 20
zakupy = 8.30
reszta = banknot - zakupy

print("Do wydania: ", reszta)

for indeks, moneta in enumerate(monety):
    if reszta >= moneta:
        ilosc = reszta // moneta
        wartosc = ilosc * moneta
        reszta = round(reszta - wartosc, 1)
        #reszta = reszta - wartosc

        wydac[indeks] = ilosc

print("Wydać: ")
for (moneta, ilosc) in zip(monety, wydac):
    print(moneta, '-', ilosc)




