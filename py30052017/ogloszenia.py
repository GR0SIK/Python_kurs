class Ogloszenie(object):

    ogloszenia = []

    def __init__(self, opis, link):
        self.opis = self.__fomatuj_opis(opis)
        self.link = link
        Ogloszenie.ogloszenia.append(self)

    def __fomatuj_opis(self, opis):
        o = str(opis).split('\n')
        return  ' '. join(o).strip()
# można importować dla konkretnej metodzie optymalizacja
    @classmethod
    def zapisz_ogloszenia(cls, nazwa_pliku):
        import pickle
        with open(nazwa_pliku, 'wb') as plik:
            pickle.dump(cls.ogloszenia, plik)

    @classmethod
    def wczytaj_ogloszenia(cls, nazwa_pliku):
        import pickle
        with open(nazwa_pliku, 'rb') as plik:
            cls.ogloszenia = pickle.load(plik, encoding='utf-8')

# definiujemy stringa aby ladnie wyswietlil
    def __str__(self):
        return '{} : {}'.format(self.opis, self.link)



