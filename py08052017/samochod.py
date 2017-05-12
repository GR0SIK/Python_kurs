# w ten sposób definiujemy klasy
# słówko kluczowe class, nazwa
class Samochod(object):
    # metoda specjalna Python'a __init__
    # metoda ta inicjalizuje obiekt podaymi argumentami
    # w tym przypadku nie podajemy dodatkowych argumentów
    def __init__(self):
        """ Inicjalizuje instancję klasy

        self - instancja klasy - ten argument jest automatycznie
        przez Pythona podawany
        """
        pass


def main():
    auto = Samochod()
    print(type(auto))


if __name__ == '__main__':
    main()