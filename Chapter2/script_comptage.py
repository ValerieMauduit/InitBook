#!/usr/bin/env python
# -*- coding : Utf-8 -*-

from comptage_fichier import *

#--- Compter les mots d'un texte et les mettre dans l'ordre décroissant 
# de nombre d'occurrences -----------------------------------------------------

# Entrée nom du fichier
nomfic = input('Nom du fichier ? ')
nb = eval(input('Nombre maxi de mots ? '))
# Liste de l'ensemble des mots du fichier
listeMots = nbmots(nomfic, liste = True, apostrophe = False, ponctuation = True)
# Comptage des occurrences
dicoMots = compte_mots(listeMots, casse = False)
# Tri du dictionnaire dans l'ordre décroissant des instances
listeOrdonnee = sorted(dicoMots.items(), key = lambda t:t[1], reverse = True)
# Affichage du dictionnaire sous forme plus sympa
nb = min(nb, len(listeOrdonnee) - 1)
for l in range(nb):
    print('{:>20s} : {:>3.0f}'.
        format(listeOrdonnee[l][0], listeOrdonnee[l][1]))
