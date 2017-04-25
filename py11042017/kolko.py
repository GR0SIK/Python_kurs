dane = input("Podaj grę: ")
print(dane[0:3])
print(dane[3:6])
print(dane[6:9])
if len(dane) == 9:

    #gra = str(dane)

    if dane.index("XXX" [0:3]) == 0:
        print("Wygrał X")

    elif dane.index("XXX" [3:6]) == 3:
        print("Wygrał X")

    elif dane.index('XXX' [6:9]) == 6:
        print("Wygrał X")


    elif dane.index("000" [0:3]) == 0:
        print("Wygrał 0")

    elif dane.index("000" [3:6]) == 3:
        print("Wygrał 0")

    elif dane.index('000'[6:9]) == 6:
        print("Wygrał 0")

else:
    print("Podaj 9 znaków !!!")