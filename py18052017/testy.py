from unittest import TestCase
from py18052017.pracownik import Pracownik
from contextlib import redirect_stdout
import io

class TestPracownik(TestCase):


    @staticmethod
    def get_print_output(testowana_funkcja):
        bufor_pamieci = io.StringIO()
        with redirect_stdout(bufor_pamieci):
            testowana_funkcja()
            return bufor_pamieci.getvalue()


    def setUp(self):
        self.prac = Pracownik("jan", "kowalski")
        self.prac.pensja = 2000

    def test_oblicz_podwyzke(self):
        wartosc_oczekiwana = 100
        wart_podw = self.prac.oblicz_podwyzke()

        self.assertEqual(wart_podw, wartosc_oczekiwana)

    def test_stanowisko_get(self):
        self.prac.stanowisko = "mechanik"

        oczek_stan = "Mechanik"

        stan = self.prac.stanowisko

        self.assertEqual(stan, oczek_stan)

    def test_wypisz_imie(self):
        metoda_testowana = self.prac.wypisz_imie
        rzeczywisty_output = TestPracownik.get_print_output(metoda_testowana)
        oczekiwany_output = "jan\n"
        self.assertEqual(rzeczywisty_output, oczekiwany_output)