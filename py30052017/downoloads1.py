import requests

def pobierz_fot(link, lokalizacja):
    """link - adres obrazka w sieci
    lokalizacja - ścieżka na dysku"""

    odpowiedz = requests.get(link)

    if odpowiedz.status_code == 200:
        bajty = 0
        try:
            with open(lokalizacja, "wb") as plik:
                for kawalek in odpowiedz.iter_content(100000):
                    ilosc = plik.write(kawalek)
                    bajty += ilosc
        except FileNotFoundError:
            print("Tworze folder i zapisuje pliki")
        print(bajty)


