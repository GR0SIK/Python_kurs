
with open("mojplik.txt", "r+") as plik:
    zawartosc = plik.read()
# sprawdza czy tekst jest w nowej lini czy ostatni znak jest \n
    if zawartosc[-1] == '\n':
        plik.write("Dane zapisane do pliku.")
    else:
        plik.write("\nDane zapisane do pliku.")

