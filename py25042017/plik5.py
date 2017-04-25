
plik = open("mojplik.txt", "r")

l = plik.readline()
print(l)

reszta_pliku = plik.read()
print("To jest reszta: \n", reszta_pliku)

plik.close()

