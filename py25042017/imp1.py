def kwadrat(a):
    return a**2

def main():
# Definujemy pustą funkcje która wykonuje zadanie która jest do niej dopisana
# wiemy to po wycięciu
    print(kwadrat(45))
    print(kwadrat(10))

# warunek się wykona jeśli będzie spełniony kod się wykona ale nie uruchmi tego
# w innym miejscu w kodzie gdzie został za importowany
if __name__ == '__main__':
    main()
