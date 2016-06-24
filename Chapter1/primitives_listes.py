#!/usr/bin/env python
# -*- coding : Utf-8 -*-

# Primitives usuelles
#-------------------------------------------------------------------------------
# Primitives de conversion de type

def s(n):
    return sum(len(str(p))/p/(p+1) for p in range(1,n+1))

for i in range(1, 8):
    print(i, end = '--> ')
    print(pow(10,i), end = '--> ')
    print(s(pow(10,i)))
    
# Itérateurs
for i, x in enumerate(liste):
    print(i, end = ' --> ')
    print(x)
    
def occurrences(liste,x):
    return(i for i,y in enumerate(liste) if y == x)
    
for i in reversed(range(12)):
     print(i, end = ' - ')
     
v1 = [randrange(42) for i in range(3)]
v2 = [randrange(42) for i in range(3)]

scal = sum(x*y for x, y in zip(v1, v2))

