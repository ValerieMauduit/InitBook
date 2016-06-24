#!/usr/bin/env python
# -*- coding : Utf-8 -*-

from time import clock
from math import sin

def f1(n):
    liste = []
    for i in range(n):
        liste += [sin(i)]
    return liste
    
def f2(n):
    liste = []
    for i in range(n):
        liste.append(sin(i))
    return liste

def f3(n):
    return [sin(i) for i in range(n)]
    
def duree(fonction, n = 10000000):
    debut = clock()
    fonction(n)
    fin = clock()
    return fin -debut

n = eval(input('Nb itérations ? '))
f1n = duree(f1, n); f2n = duree(f2, n); f3n = duree(f3, n)
print(f1n, f2n, f3n)
print('Gain 1 : {:.2f}%'.format(100 * ((f1n - f2n)/ f1n)))
print('Gain 2 : {:.2f}%'.format(100 * ((f2n - f3n)/ f2n)))
print('Gain total : {:.2f}%'.format(100 * ((f1n - f3n)/ f1n)))

