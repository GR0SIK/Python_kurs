class Pracownik(object):

    roczna_podw = 5
    ilosc_pracownikow = 0

    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        self.wynagrodzenie = None
        Pracownik.ilosc_pracownikow +=1

    def ustaw_pensje(self, kwota):
        if kwota > 10000:
            self.wynagrodzenie = 10000
        else:
            self.wynagrodzenie = kwota

    def daj_podwyzke(self):
        self.wynagrodzenie += self.wynagrodzenie * (self.roczna_podw / 100)

    def __del__(self):
        Pracownik.ilosc_pracownikow -= 1

    def __str__(self):
        return "{} - {} ma wynagrodzenie: {}".format(self.imie, self.stanowisko, self.wynagrodzenie)

    @classmethod
    def ustaw_roczna_podw(cls, ilosc_p_proc):
        cls.roczna_podw = ilosc_p_proc

    @classmethod
    def Pracownik_wynagr(cls, imie, stanowisko, pensja):
        """Alternatywny inicjalizator"""
        prac = Pracownik(imie, stanowisko)
        prac.ustaw_pensje(pensja)
        return prac

    @staticmethod
    def sprawdz_pesel(pesel):
        if len(str(pesel)) != 11:
            print("Pesel nieprawidłowy")

Pracownik.sprawdz_pesel(730039123202)

prac1 = Pracownik("Adam", "Kowal")
prac2 = Pracownik.Pracownik_wynagr("Jakub", "Spawacz", 5000)

print(prac1)
print(prac2)