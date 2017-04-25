a = 3
b = 4
x = b / (2.0 + a)

print(x)

#print("{:.3}")
print("{:.17f}".format(x))
# print("{0:.17f}".format(x)) - można też tak 17 oznacza miejsc po przecinku f oznacza flout

print("\n")
#{} - miejsce na zmienną
print("zmienna a:{} zmienna b:{}".format(a,b))

# można wskazać którą zmienną
print("zmienna a:{0} zmienna b:{0}".format(a,b))

print("\n")

print(True)
print(False)
print(type(True))
print("\n")
print(True == True)
print(True != True)
print(False != True)
# == służy do sprawdzania czy coś jest równe
