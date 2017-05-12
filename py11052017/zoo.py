from py11052017.zwierze import Zwierze
from py11052017.czlowiek import Czlowiek
from py11052017.czlowiek import Student
animall = Zwierze("Mammut")
animal2 = Czlowiek("Janek")

print(animall.imie)
print(animal2.imie)

animall.biega()
animal2.biega()

Zwierze.biega(animal2)

student1 = Student("Janek", 43344)
print(student1.nr_indeksu)