import os
from py23052017.poczta_zalacznik import Poczta
from py23052017.secrets import *


poczta = Poczta(moj_login, moje_haslo)

adresaci = [moj_login]
temat = "Hello from Grzech - załączniki"
tresc = "To są załączniki"
root = "c:\\zdjecia"
#zalaczniki = [os.path.join(root, plik) for plik in os.listdir(root)]
#print(zalaczniki)

zalacz = []
for plik in os.listdir(root):
    pelna_sciezka = os.path.join(root, plik)
    zalacz.append(pelna_sciezka)
poczta.wyslij_wiadomosc(adresaci, temat, tresc,zalacz)

#zalaczniki = ["c:\\zdjecia\\001.jpg", "c:\\zdjecia\\002.jpg", "c:\\zdjecia\\003.jpg"]
#poczta.wyslij_wiadomosc(adresaci, temat, tresc,zalaczniki)

