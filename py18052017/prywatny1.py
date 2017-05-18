class Zawodnik(object):
#   def __init__(self, imie, dyscyplina, numer):
    def __init__(self, imie, dyscyplina):
        self.name = imie
        self.dyscy = dyscyplina
#       self.numer_koszulki = numer
#       self.numer_koszulki = None
# prywatna zmienna
        self.__numer_koszulki = None

    @staticmethod
# pomoc można wykorzystac tylko w klasie
    def __sprawdz_numer(numer):
        """ Ma sprawdzic czy numer koszulki jest poprawny"""
        if numer < 0 or numer > 99:
            return False
        else:
            return True

    # def zmien_numer(self, nowy_numer):
    #     if nowy_numer < 0 or nowy_numer > 99:
    #         print("Niewłaściwy numer")
    #     else:
    #         self.__numer_koszulki = nowy_numer


    def zmien_numer(self, nowy_numer):
        if not Zawodnik.__sprawdz_numer(nowy_numer):
            print("Niewłaściwy numer")
        else:
            self.__numer_koszulki = nowy_numer

# przy prywatnych trzeba kazać aby zwrócił
    def daj_numer_koszulki(self):
        return self.__numer_koszulki
    #
    # def __sprawdz_numer(self, numer):
    #     """ Ma sprawdzic czy numer koszulki jest poprawny"""
    #     if numer < 0 or numer > 99:
    #         return False
    #     else:
    #         return True


koszykarz = Zawodnik("Michael Jordan", "Koszykówka")
koszykarz.zmien_numer(23)
#   print(koszykarz.name, koszykarz.numer_koszulki)

print(koszykarz.name, koszykarz.daj_numer_koszulki())

# pilkarz = Zawodnik("Robert Lewandowski", "Nożna")
# pilkarz.zmien_numer(123)
# print()
# print(pilkarz.__dict__)
# pilkarz.numer_koszulki = 234
# print()
# print(pilkarz.__dict__)
# print(pilkarz.name, pilkarz.numer_koszulki)

print(Zawodnik.__dict__)
