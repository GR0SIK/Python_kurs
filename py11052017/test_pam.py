# klasy są typami referenycjnymi

class Og(object):
    def __init__(self, cena):
        self.cena = cena


a = Og(3000)
b = a
b.cena = 2000

print(a.cena)