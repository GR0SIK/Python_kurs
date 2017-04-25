# poczliczyc ilosc liczb parzystych i nieparzystych

zakres = range(23, 3821732)

ilosc_parzyste = 0
ilosc_nieparzyste = 0

for i in zakres:
    if i % 2 == 0:
        ilosc_parzyste +=1
    else:
        ilosc_nieparzyste +=1


# drukuje ilość
print("Ilość parzystych: {}, nieparzystych {}".format(ilosc_parzyste, ilosc_nieparzyste))