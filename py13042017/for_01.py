#   petla for

# rangr

x = range(100)
print(x)
# liczba zmienna gdzie umieszczana są wartości
for liczba in x:
    print(liczba * liczba)


for litera in "Aleksandra":
    print(litera)

for litera in "Aleksandra"[::-1]:
    print(litera)

for litera in "Aleksandra":
    print(litera.capitalize())

for litera in "Aleksandra":
       print("Nie korzystam z litery!")

imie = "Hermenegilda"
indeks = 0
for c in imie:
    print(indeks, c)
    indeks += 1

imie = "Hermenegilda"

for i, k in enumerate(imie):
    print(i, k)