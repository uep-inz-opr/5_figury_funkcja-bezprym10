from cmath import sqrt
import math


def pole_kolo(x):
    wynik = math.pi * x[0] * x[0]
    return round(wynik, 2)

def pole_prostokat(x):
    wynik = x[0] * x[1]
    return round(wynik, 2)

def pole_trojkat(x):
    s = (x[0] + x[1] + x[2])/2
    wynik = math.sqrt(s*(s - x[0]) * (s - x[1]) * (s - x[2]))
    return round(wynik, 2)

def pole_figury(x):
    if len(x) == 1:
        return pole_kolo(x)
    elif len(x) == 2:
        return pole_prostokat(x)
    elif len(x) == 3:
        return pole_trojkat(x)

def suma_pol(lista_figur):
    pole_cale = 0
    for figura_dane in lista_figur:
        pole_cale += pole_figury(figura_dane)
    return pole_cale

def run():
    liczba_figur = int(input())
    lista_figur = []
    for i in range(liczba_figur):
        figura_dane = input().strip().split(' ')
        for j in range(len(figura_dane)):
            figura_dane[j] = float(figura_dane[j])
        if len(figura_dane) > 3:
            return "Błąd: można podać maksymalnie 3 liczby"
        lista_figur.append(figura_dane)
    return suma_pol(lista_figur)


pole = run()
print(pole)
