class Ogloszenie(object):

    def __init__(self, rynek, cena, pietro, metry, miejscowosc, tel):

        self.rynek = rynek
        self.cena = cena
        self.pietro = pietro
        self.metry = metry
        self.miejscowosc = miejscowosc
        self.tel = tel



    def wyswietl(self):
        print("Nieruchomość {}, cena {} PLN, kontakt do sprzedjącego: {}"\
              .format(self.rynek, self.cena, self.tel))
#.format w miejsce {} wskazuje dane ze zmiennych

    def zmien_tel(self, nowy_tel):
        if str(len(nowy_tel)) >= 6:
            self.tel = nowy_tel








