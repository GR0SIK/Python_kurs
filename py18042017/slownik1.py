# dict

slownik = {}

print(slownik)
print(type(slownik))

slownik2 = {'imie': 'Adam',
            'nazwisko':'Kowalski',
            1:'jedyneczka'}

print(slownik2)
print(len(slownik2))

print(slownik2[1])
print(slownik2.keys())
print(slownik2.values())

slownik2['wiek'] = 32
print(slownik2)

del slownik2['wiek']
print(slownik2)