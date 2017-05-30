import requests
from bs4 import BeautifulSoup

# Alt Enter instaluje brakujące moduły

response = requests.get("http://trojmiasto.pl")
print(response.status_code)

# wykonując ta metode sprawdza czy strona jest status 200
# jeśli jest 200 wykonuje dalej kod
#response.raise_for_status()

# to samo tylko z opcją id
if response.status_code == 200:
    with open("trojmiasto.txt", "w", encoding="utf-8") as plik:
        plik.write(response.text)

# html parser - nie bedzie pokazywac bledu z kompatiblinoscia wstecz
trojmiasto_soup = BeautifulSoup(response.text, "html.parser")

linki = trojmiasto_soup.select(".news-list li a")
#print(linki)

for link in linki:
    print(link.getText())
    print(str(link))
    print(link.get('id'))
    print(link.get('title')), link.get('href')
