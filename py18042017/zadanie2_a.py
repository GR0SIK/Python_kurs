import copy

nabial = ["mleko", "jajka", "ser"]
chemia = ["domestos", "plyn do naczyn"]

zakupy_kwiecien = [nabial, chemia]
# print("kwiecien: ", zakupy_kwiecien)

zakupy_maj = zakupy_kwiecien.copy()
# print("maj: ", zakupy_maj)

zakupy_czerwiec = [x for x in zakupy_kwiecien]
# print("Zakupy czerwiec: ", zakupy_czerwiec)

# kopiuje z kwietnia pierwotną a nie adres w pamięci
zakupy_lipiec = copy.deepcopy(zakupy_kwiecien)

zakupy_kwiecien[1].append("gąbka")
print("kwiecien: ", zakupy_kwiecien)
print("maj: ", zakupy_maj)
print("czerwiec: ", zakupy_czerwiec)
print("lipiec: ", zakupy_lipiec)

