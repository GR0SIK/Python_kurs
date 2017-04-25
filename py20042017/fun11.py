def czy_w_zakresie(liczba, zakres):
    '''
    Sprawdza czy podana liczba jest w zakresie. 
    Zwraca True jeśli jest.
    :param liczba: -> bool 
    '''
    # dwie zmienne
    # jeśli chcemy sprawdzic czy coś jest w czyms
    if liczba in zakres:
        return True
    else:
        return False

# x = 23
# y = range(1,23)
# wynik = czy_w_zakresie(x, y)
# print(wynik)
# funkcje można używąc w innym miejscu w kodzie
liczby = [23, 345, 22465, 454, 3543, 34, 35]
for liczba in liczby:
    print(czy_w_zakresie(liczba , range(100)))
