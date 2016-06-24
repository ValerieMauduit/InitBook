#!/usr/bin/env python
# -*- coding : Utf-8 -*-

# Intégrale par méthode de Monte-Carlo

from math import *
from random import *

# Fonction de calcul approximatif
def intMC(fun,a,b,n):
    if a > b:
        a, b = b, a
    somme = 0
    for i in range(n):
        somme += fun(uniform(a, b))
    return (b - a) / n * somme
    

# Tests - affichages finaux
print('Valeur officielle de Pi : {:20.12f}'.format(pi))
foncPi = lambda x: sqrt(1 - x * x)
calcul = 4 * intMC(foncPi,0 , 1, 1000)
print('Valeur calculée par intégrale : {:14.12f}'.format(calcul))
print("Taux d'erreur : {:5.2}%".format((calcul - pi) / pi * 100))
