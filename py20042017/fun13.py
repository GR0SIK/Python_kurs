# funkcja sprawdzajaca czy podany string jest palindromem

# import 20042017.fun7.odwr_str
from py20042017.fun7 import *


#def odwr_str(zdanie):
#    return zdanie[::-1]


def odwroc_input():
    zdanie = input("Podaj zdanie: ")
    return zdanie [::-1]


def czy_palindrom(fraza):
    '''Sprawdza czy fraza jest palindromem'''
    odwocona = odwr_str(fraza)
    #
    # for litera1, litera2 in zip(fraza, odwocona):
    #     if litera1 != litera2:


    for litera1, litera2 in zip(fraza, odwocona):
        if litera1 == litera2:
            continue
        else:
            return False

    return True

print(czy_palindrom("kajak"))
print(czy_palindrom("Jedzenie"))