# funkcja zwraca odwrócony string

def odwr_str(zdanie):
    return zdanie[::-1]


odwocony = odwr_str("Ala ma kota")
print(odwocony)

def odwroc_input():
    zdanie = input("Podaj zdanie: ")
    return zdanie [::-1]

print(odwroc_input())
print(odwroc_input())

