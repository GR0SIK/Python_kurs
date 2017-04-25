def kwadrat(liczba):
    """    Zwraca kwadrat podanej liczby    """
    return liczba**2

def pole_prostkata(bok_a, bok_b):
    """Zwraca pole prostokonta"""

 #   return bok_a * bok_b
    if bok_a == bok_b:
        return kwadrat(bok_a)
    else:
        return bok_a*bok_b

print(pole_prostkata(5, 4))
print(pole_prostkata(5, 5))