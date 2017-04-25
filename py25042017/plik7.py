
# lista imion

lista = ['Ala', 'Ola', 'Jola']

# plik nie istnieje
# otwieramy w trybie w albo a
with open("imiona.txt", "w") as plik:
    # to zapisze element jednym ciagiem
    # plik.writelines(lista)

    for element in lista:
        plik.write(element + "\n")