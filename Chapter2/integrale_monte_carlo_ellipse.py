#!/usr/bin/env python
# -*- coding : Utf-8 -*-

# Intégrale par méthode de Monte-Carlo

from math import *
from random import *

# Fonction de calcul approximatif d'aire d'une ellipse
def ellipse(a,b,n):
    if b > a: 
        a, b = b, a
    somme = 0
    c = sqrt(a * a - b * b) # Foyers de l'ellipse = (+/-c ; 0)
    for i in range(n):
        x = uniform(-a, a)
        y = uniform(-b, b)
        # Distance entre point (x,y) et foyer 1 :
        if hypot(x/a, y/b) <= 1:
            d1 = hypot(x - c, y)
            d2 = hypot(x + c, y)
            somme += d1 + d2
    return (4 * a * b) / n * somme
    

# Tests - affichages finaux
a = 12
b = 42
if a > b:
    aire = 2 * pi * b / 3 * (3 * a * a - b * b)
else:
    aire = 2 * pi * a / 3 * (3 * b * b - a * a)
print("Valeur officielle aire de l'ellipse : {:12.2f}".format(aire))
calcul = ellipse(a, b, 100000) 
print('Valeur calculée par intégrale : {:12.2f}'.format(calcul))
print("Taux d'erreur : {:5.2}%".format((calcul - aire) / aire * 100))
