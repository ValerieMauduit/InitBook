#!/usr/bin/env python
# -*- coding : Utf-8 -*-

# Les listes
#-----------------------------------------------------------------------------

L = ['Valérie', 43, 'Christian', 41, 'Adèle', 12,
    'Lise', 11, 'Garance', 9]
print(L[1:-1])
L[3:3] = ['Boudin blanc'] # insère un/plusieurs élément(s)
L[3] = 'Boudin blanc' # remplace un élément par un autre

copieL = L[:] # Sinon on copie le pointeur

# Si listes emboîtées :
import copy
L2 = copy.deepcopy(L)

# Méthodes sur les listes
# REMPLACENT liste par liste modifiée
#L.append(x)
#L.extend(L)
#L.insert(i, x)
#L.remove(x)
#L.pop([i])
#L.index(i)
#L.count(x)
#L.sort()
#L.reverse()

def cherche(L,x):
    n = 0
    while n < len(L):
        if L[n] == x:
            return True
        else:
            n += 1
    return False
    


# Les listes par compréhension
[3*x for x in range(4)]
from math import *
[sin(x) for x in test if x**2 > 100]
[x*sin(y) for x in test for y in range(4)]
l = [[1, 2, 3], [40, 50, 60], [700, 800, 900]]
[x for xl in l for x in xl]

