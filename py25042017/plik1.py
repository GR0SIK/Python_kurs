# otwieramy plik

# plik = open("C:\\Users\\admin\\Desktop\\Kurs\\Python_iSA\\py25042017\\mojplik.txt")

plik = open("mojplik.txt")
# wyswietla tylko kolejne linijke
linijka = plik.readline()
print(linijka)

# po wszystkinm plik musi zostac zamkniety
plik.close()