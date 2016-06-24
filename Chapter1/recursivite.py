#!/usr/bin/env python
# -*- coding : Utf-8 -*-

# Récursivité
#-----------------------------------------------------------------------------

import sys
sys.setrecursionlimit(100000000)

def expFor(n):
    v = 1
    for x in range(1, n+1):
        v *= x
    return v
        
def expRec(n):
    if n == 0:
        v = 1
    else:
        v = n * expRec(n-1)
    return v
        
def horner(polynome, x0): # Calcul de la valeur du polynôme en x0
    if len(polynome) == 1:
        return polynome[0]
    else:
        polynome[1] = polynome[0] * x0 + polynome[1]
        return horner(polynome[1:],x0)
        
coefs = eval(input('Coefficients ? '))
print(horner(coefs, valeur))

if __name__ == "__main__":    # Test de développement de la bibliothèque
    # Sert quand j'appelle directement ce fichier par commande Python
    print('=== Début des tests de la bibliothèque recursivite ===')
    l = [randrange(20) for i in range(30)]
    print('-- Test de la fonction expFor -------------------')
    valeur = eval(input("Nombre ? "))
    print("L'exponentielle de {:.0f} est {:.0f} "
        "(méthode for)".format(valeur, expFor(valeur)))
    print("-- Test de la fonction expRec -------------------")
    print("L'exponentielle de {:.0f} est {:.0f} "
        "(méthode rec)".format(valeur, expRec(valeur)))
    print("-- Test de la fonction horner -------------------")
    print("  Calcul de la valeur d'un polynôme ")
    coefs = eval(input('Coefficients ? '))
    print(horner(coefs, valeur))
    print('=== Fin des tests de la bibliothèque Lprint =====')
