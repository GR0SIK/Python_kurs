import os, shutil, send2trash

print(shutil.disk_usage('c:\\'))
# zmiana sciezki gdzie w systemie ma wykonac zadanie
os.chdir("c:\\")
print(os.getcwd())
# twory folder
# os.mkdir("pytapl")
#kopiowanie folderow
# shutil.copytree("c:\\zdjecia", "c:\\pytapl\\z")

# zawartosc = os.listdir("c:\\pytapl\\z")
# print(zawartosc)
#
# for plik in zawartosc:
#     print(plik)

for folder, podfoldery, pliki in os.walk("c:\\pytapl"):
    print("Obecny folder to: ", folder)
    for podfolder in podfoldery:
        print("Podfolder: {} w folderze: {}".format(podfolder, folder))
    for plik in pliki:
        print("Plik {} w folderze {}".format(plik, folder))
    print()