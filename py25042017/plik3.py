
# aby nie czytal nowej lini musimy dac argument end=""
print(plik.readline(), end='')

tresc = plik.read(16)
print(tresc)

plik.close()