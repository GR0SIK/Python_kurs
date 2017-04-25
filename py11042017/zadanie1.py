# przyjąć input od użytkownika
dane = input("Podaj grę: ")
# sprawdzic czy string ma 9 znaków
if len(dane) == 9:
# jeśli tak
# sprawdze x poziomo
    if dane.index("XXX") == 0:
        print("Wygrał X")
# wygrana x
    # sprawdze x pionie
    elif dane.index("X00X00X") == 1:
        print("Wygrał X")

        # wygrana x
    # sprawdze x ukosnie
        # wygrana x
# w przciwnym razie sprawdze 0

    # j.w

# w przeciwnym razie
    # remis

else:
    print("Podaj 9 znaków !!!")