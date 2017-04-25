zdanie = input("Napisz coś tam: ")

litery = 0
cyfry = 0

for znak in zdanie:
    if znak.isdigit():
        cyfry += 1
    elif znak.isalpha():
        litery += 1

print("Litery: ", litery)
print("Liczby: ", cyfry)