#!/usr/bin/env python
# -*- coding : Utf-8 -*-

from sys import argv

# Passer des arguments dans un script appelé en ligne
#fichier = open(argv[1],'r')
#if fichier:
#    print('Le fichier {} existe'.format(argv[1]))
#else:
#    print("Erreur, ce fichier n'existe pas")

# Ecriture de fichier standard
nom = 'ficwrite.txt'
fichier = open(nom, 'w')
for n in range(10):
    fichier.write("Ceci est la ligne {}\n".format(n))
fichier.close()

# Ecriture de listes dans un fichier
nom = 'ficwritelines.txt'
fichier = open(nom, 'w')
for n in range(10):
    liste = ['Toto', 'école', "lycée "]
    fichier.writelines(liste)
    fichier.writelines("Ceci est la ligne {}\n".format(n))
fichier.close()

# Lecture, méthode 1
fichier = open(nom, 'r')
liste = fichier.read()
print(liste)
fichier.close()

# Ajout en fin de fichier
fichier = open(nom, 'a')
fichier.write('Et on ajoute ça')

# Lecture sous forme de liste
fichier = open(nom, 'r')
liste = fichier.readlines()
print(liste)
fichier.close()

# Lecture, méthode alternative COOL
fichier = open(nom, 'r')
for l in fichier:
    print(l, end = ' -*- ')
fichier.close()


