import string

def czy_pangram(fraza):
    '''Sprawdza czy fraza jest pangramem'''
    for litera in string.ascii_lowercase:
        if litera not in str(fraza).lower():
            return False
    return True

print(czy_pangram("abcDE"))
print(czy_pangram("The quick brown fox jumps over the lazy dog"))

