
import pickle

baza = ['Bartosz', 'Moje', '33']

# zapisywanie

# with open("ogorek.txt", "wb") as plik:
#     pickle.dump(baza, plik)

# odczytywanie

with open("ogorek.txt", "rb") as plik:
    baza_no = pickle.load(plik)

    print(baza_no)

