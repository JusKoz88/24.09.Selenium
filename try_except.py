cena = input('daj cene ')
try:
        cena = float(cena)
        print('zrzutowano do float')
except:
    print('cena ma typ',type(cena))
    cena = 100
    print('zla cena, przyjmuje 100')
wynik = cena * 2.1

print(wynik)