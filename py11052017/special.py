from py11052017.ogloszenie1 import Ogloszenie

o1 = Ogloszenie(2000, miejscowosc="Sopot")
o2 = Ogloszenie(3000, miejscowosc="Gdynia")

print(o1)
print(o2)

suma = o1 + o2
print("Suma wynosi:", suma)

# del usuwa wszystkie obiekty
#del o1