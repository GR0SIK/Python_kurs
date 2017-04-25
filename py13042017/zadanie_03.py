zdanie = input("Napisz coś tam: ")

samogloski = 'aeiouy'
litery = 0
cyfry = 0
il_samogl = 0
il_spolgl = 0

for znak in zdanie:
    if znak.isdigit():
        cyfry += 1
    elif znak.isalpha():
        litery += 1
        if znak in samogloski:
            il_samogl +=1
        else:
            il_spolgl +=1
print("Litery: ", litery)
print("Liczby: ", cyfry)
print("Samogłoski: ", il_samogl)
print("Spółgłoski: ", il_spolgl)