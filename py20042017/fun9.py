# zmienna na poziomie globalnym

imie = "jola"

def drukuj_imie(imie_2):
    global imie
    imie = "ania"
    imie = imie.capitalize()
    imie_2 = str(imie_2).capitalize()

    print(imie, imie_2)

drukuj_imie("gosia")
print(imie)