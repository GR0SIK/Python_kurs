from py30052017 import ogloszenia
from py23052017.secrets import *
from py23052017.poczta_zalacznik import Poczta

ogloszenia.Ogloszenie.wczytaj_ogloszenia("ogloszenia.dat")

ads = ogloszenia.Ogloszenie.ogloszenia

tekst = ""

for ad in ads:
    tekst += ad.opis + ad.link
    tekst += "-------------\n"

#print(tekst)

# tutaj wysylamy tekst

mailer = Poczta(moj_login, moje_haslo)
mailer.wyslij_wiadomosc([moj_login], "ogloszenia", tekst)