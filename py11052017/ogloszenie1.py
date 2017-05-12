class Ogloszenie(object):
    """Definiuje ogłoszenie w portalu otodom"""

    def __init__(self, cena, metraz=None, miejscowosc=None, tel=None, id = None):
        self.cena = cena
        self.metraz = metraz
        self.miejscowosc = miejscowosc
        self.tel = tel
        self.zdjecia = None
        self.id = None

    def __str__(self):
        return "Miejscowosc {} - cena: {}".format(self.miejscowosc, self.cena)

    def __add__(self, other):
        return self.cena + other.cena

    def __del__(self):
        print("Ogłoszenie {} {} usunięte".
              format(self.miejscowosc, self.cena))

    def dodaj_zdjecie(self, foto):
        if self.zdjecia == None:
            self.zdjecia = []
            self.zdjecia.append(foto)
        else:
            self.zdjecia.append(foto)

    def wyswietl(self):
        print("Nieruchomość {} m2, cena {} PLN, kontakt do sprzedającego: {}"\
              .format(self.metraz, self.cena, self.tel))

    def zmien_tel(self, nowy_tel):
        if str(len(nowy_tel)) >= 6:
            self.tel = nowy_tel

    def pokaz_zdjecie(self):
        if self.zdjecia != None:
            print("Oto zdjecie................")
        else:
            print("Nieprawidłowe zdjęcie!")