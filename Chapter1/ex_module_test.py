#!/usr/bin/env python
# -*- coding : Utf-8 -*-

def lprint(liste, largeur, forme):
    '''lprint(liste, largeur, forme)'''
    n = len(liste)
    lignes = n // largeur
    print('[', end = '')
    for i in range(n):
        s = '{:' + forme + '}'      # Définit le format de sortie des nombres
        if i < n-1:
            print(s.format(liste[i]), end = ',')
        else:
            print(s.format(liste[i]), end = ']')
        if i > 0 and i % largeur ==  largeur - 1:
            print()                 # Passage à la ligne
            print(' ', end = '')    # Début de ligne suivante
    print()
    
from random import *
if __name__ == "__main__":    # Test de développement de la bibliothèque
    # Sert quand j'appelle directement ce fichier par commande Python
    print('=== Début des tests de la bibliothèque Lprint ===')
    l = [randrange(20) for i in range(30)]
    print('-- Test de la fonction lprint -------------------')
    print(l)
    lprint(l,8,'3.0f')
    print()
    print('=== Fin des tests de la bibliothèque Lprint =====')
