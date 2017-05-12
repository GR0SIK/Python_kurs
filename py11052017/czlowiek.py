from py11052017.zwierze import Zwierze

class Czlowiek(Zwierze):
    def __init__(self, imie):
        Zwierze.__init__(self, imie)

    def biega(self):
        print("Człowiek {} biega".format(self.imie))


class Student(Czlowiek):
    def __init__(self, imie, indeks):
        super().__init__(imie)
        self.nr_indeksu = indeks