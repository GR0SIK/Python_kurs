# program usuwający duplikaty z listy

lista = [10,20,30,40,20,45,54,45,90,90,101]
lista_bez_duplik = []

# num zmienna

for num in lista:
    if num not in lista_bez_duplik:
        lista_bez_duplik.append(num)

print(lista_bez_duplik)


