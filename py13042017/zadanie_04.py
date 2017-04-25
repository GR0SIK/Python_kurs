import string

zdanie = input("Napisz coś tam: ")

samogloski = 'aeiouy'
litery = 0
cyfry = 0
male_litery = 0
duze_liter = 0

for znak in zdanie:
    if znak.isdigit():
        cyfry += 1
    elif znak.isalpha():
        litery += 1
        if znak in string.ascii_lowercase:
            male_litery +=1
        else:
            duze_liter +=1
print("Litery: ", litery)
print("Liczby: ", cyfry)
print("Małe litery: ", male_litery)
print("Duże litery: ", duze_liter)

