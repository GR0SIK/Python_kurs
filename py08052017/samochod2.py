class Samochod(object):
    """Opisuje właściwości samochodu"""

    def __init__(self, marka, model, kolor):
        """
        Inicjalizuje obiekt specyficznymi danymi.
        :param marka: Marka samochodu 
        :param model: Model samochodu
        :param kolor: Kolor samochodu
        """
        self.marka = marka
        self.model = model
        self.color = kolor
        self.czy_jedzie = False
        self.silnik = None

    def jedz(self):
        """Rusza samochód"""
        print(self.marka, ": Jadę")
        self.czy_jedzie = True

    def zatrzymaj(self):
        """Zatrzymuje samochód"""
        self.czy_jedzie = False

