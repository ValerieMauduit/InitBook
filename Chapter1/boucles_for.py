#!/usr/bin/env python
# -*- coding : Utf-8 -*-

# Les boucles FOR
#-----------------------------------------------------------------------------

a = range(43)
b = list(a)

for n in L:
    b.append(42)
    b.append(n)
    print(n)
print(b)

def somme(liste):
    s = 0
    for x in liste:
        s += x
    return s

def maxi(liste):
    m = liste[0]
    for x in liste:
        if x > m:
            m = x
    return m
    
test = eval(input('Liste ? '))
print(somme(test))
print(maxi(test))

def enlever(liste,x):
    n = 0
    for x1 in liste:
        if x1 == x:
            return liste[:n] + liste[n+1:]
        else:
            n += 1
    return False

test = [12, 42, 33, 7.7, 89, 100, .01, 42]
print('La liste est {}'.format(test))
x = eval(input('Nombre ? '))
print("J'ai retiré {} et j'obtiens {}".format(x, enlever(test,x)))

def enleve_sep(liste,n):
    if n < len(liste):
        elem = liste[n]
        liste = liste[:n] + liste[n+1:]
        return elem, liste
    return False, liste

n = eval(input('Position ? '))
e2, l2 = enleve_sep(test, n)
print("J'enlève le nombre en position {} (c'est {}), et "
    "j'obtiens {}".format(n, e2, l2))
    
def indexVM(liste,x):
    n = 0
    for x1 in liste:
        if x1 == x:
            return n
        else:
            n += 1
    return False
    
print("Le nombre {} est à l'index {}".format(x, indexVM(test, x)))

def compte(liste, x):
    n = 0
    compteur = 0
    for x1 in liste:
        if x1 == x:
            compteur += 1
    return compteur
    
print("Il y a {} fois {} dans la liste {}".format(compte(test, x), x, test))

def renverser(liste):
    l2 = []
    for x in liste:
        l2 = [x] + l2
    return l2
    
print("Liste renversée : {}".format(renverser(test)))

