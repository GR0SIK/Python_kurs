lista = [1,2,3,4,5,6,7,8,9]

lista2 = []

for elemenet in lista:
    lista2.append(elemenet*elemenet)

# print(lista2)
# **2 podniesienie do kwadratu
lista3 = [elemenet**2 for elemenet in lista]
print(lista3)

lista4 = [elemenet**2 for elemenet in lista if elemenet%3 == 0]
print(lista4)

