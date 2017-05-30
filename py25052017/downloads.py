import requests

#odpowiedz = requests.get("http://gdansk.pl")
#print(odpowiedz.status_code)

obrazek = "https://img.ivme.pl/e7c3619f-326d-46b1-a23a-7306f62c41a7.jpg"

odpowiedz = requests.get(obrazek)
print(odpowiedz.status_code)
# wb - oznacza write binarnie

bajty = 0
with open("pliczek.jpg", "wb") as plik:
    for kawalek in odpowiedz.iter_content(100000):
        ilosc = plik.write(kawalek)
        bajty += ilosc
print(bajty)


# with open("pliczek.jpg", "wb") as plik:
#     for kawalek in odpowiedz.iter_content(100000):
#         bajty = plik.write(kawalek)
#         print(bajty)
