#!/usr/bin/env python
# -*- coding : Utf-8 -*-

# Renvoyer le nombre de lignes d'un fichier -----------------------------------
def nblines(nomfic):
    """Compte le nombre de lignes dans un fichier nommé nomfic"""
    fic = open(nomfic, 'r')
    l = fic.readlines()
    return len(l)
    
# Renvoyer le nombre de mots d'un fichier -------------------------------------

def nbmots(nomfic, **keywords):
    """Compte le nombre de mots dans un fichier nommé nomfic
    
    Mots clés : 
    - apostrophe = True si on sépare en deux mots les chaînes de
        caractères contenant une apostrophe
    - ponctuation = True si on retire les ponctuations avant de 
        compter
    - liste = True si au lieu de fournir le nombre de mots on fournit 
        la liste des mots du fichier""" 
    with open(nomfic, 'r') as fic:
        l = fic.read()
        # Remplacer les apostrophes par des espaces - si option
        if keywords.get('apostrophe'):
            l = l.replace("'", "' ")
        # Retirer les ponctuations - si option
        if keywords.get('ponctuation'):
            l = l.replace(".", " ")
            l = l.replace(",", " ")
            l = l.replace(";", " ")
            l = l.replace("!", " ")
            l = l.replace("?", " ")
            l = l.replace(":", " ")
            l = l.replace('"', ' ')
        # Renvoyer plutôt la liste des mots que leur compte - si option
        if keywords.get('liste'):
            return l.split()
        else:
            return len(l.split())
    fic.close()
    
# Compter les instances de chaque mot dans une liste --------------------------
# Par exemple : pour compter dans un fichier 
def compte_mots(liste, **keywords):
    """Compte le nombre d'instances de chaque mot dans une liste de mots 
    Attention : en fait, si on a mis des nombres ou d'autres types d'objets,
    ils seront comptés de la même manière
    
    Mot clé :
    - casse = True si la casse est prise en compte ('Mot' est différent de
    'mot') - Valeur par défaut = True"""
    dico = dict()
    # Remplacement de tous les mots par des minuscules (si casse = False)
    if keywords.get('casse') == False:
        for n in range(len(liste)):
            liste[n] = liste[n].lower()
    # Si le mot est déjà dans le dictionnaire --> rien
    # S'il n'est pas dedans : compter ses occurrences dans la liste
    for mot in liste:
        if dico.__contains__(mot) == False:
            dico.__setitem__(mot, liste.count(mot))
    # Ensuite on trie du plus courant au moins courant
    return dico

# Tests de la librairie -------------------------------------------------------
if __name__ == '__main__':
    print('=== Début des tests du module comptage_fichier ====================')
    print('Fonction nblines - Nombre de lignes dans le script module : '
        '{}'.format(nblines('comptage_fichier.py')))
    print('')
    print('Fonction nbmots - Nombre de mots dans le script module : '
        '{}'.format(nbmots('comptage_fichier.py')))
    ltest = nbmots('comptage_fichier.py', 
        liste = True, apostrophe = True, ponctuation = True)
    print('Fonction nbmots - Liste des mots dans le script module : '
        '{}'.format(ltest))
    print('')
    print("Fonction compte_mots - Nombre d'instances de chaque mot "
        "dans le fichier de test : "
        '{}'.format(compte_mots(ltest)))
    print('=== Fin des tests du module comptage_fichier ======================')
    
