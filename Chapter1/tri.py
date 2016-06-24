#!/usr/bin/env python
# -*- coding : Utf-8 -*-

# Les tris
#-----------------------------------------------------------------------------

def triSelec(liste):
    if len(liste) == 1:
        return liste
    else:
        m = max(liste)
        return [m] + triSelec(liste[:liste.index(m)] + 
            liste[liste.index(m)+1:])

def insertion(liste,n):
    index = n
    while (liste[n] > liste[index-1]) and (index > 0):
        index -= 1
    return liste[:index]+liste[n:n+1]+liste[index:n]+liste[n+1:]

def triSelec2(liste):
    for n in range(len(liste)):
        liste = insertion(liste,n)
    return liste

def triRapide(liste):
    if len(liste) == 0:
        return []
    else:
        l = triRapide([x for x in liste if x > liste[0]])
        l = l + liste[0:1]
        l = l + triRapide([x for x in liste[1:] if x <= liste[0]])
        return l

if __name__ == "__main__":    # Test de développement de la bibliothèque
    print('=== Début des tests de la bibliothèque tri ======')
    from random import randrange
    n = 10; liste = [randrange(100) for i in range(n)]
    print(liste)
    print('--- Test de la fonction triSelec ----------------')
    1 = triSelec(liste)
    print("Le tri 1 donne {}".format(l1))
    print('--- Test de la fonction triSelec2 ---------------')
    l2 = triSelec2(liste)
    print("Le tri 2 donne {}".format(l2))
    print('--- Test de la fonction triRapide ---------------')
    l3 = triRapide(liste)
    print("Le tri 3 donne {}".format(l3))
    print('=== Fin des tests de la bibliothèque tri ========')
