#!/usr/bin/env python
# -*- coding : Utf-8 -*-

# Les variables
#-------------------------------------------------------
a = 12
a, id(a), type(a)
b = 34
a, b = b, a
a += 3
b *= 9

# Les fonctions
#-------------------------------------------------------
def f(x):
    """C'est ici qu'on met la doc de la fonction
    - sur plusieurs lignes si on veut."""
    return x ** 3 + x ** 2 - 6
    
# Ecriture et lecture
#-------------------------------------------------------
# Je ne verrai pas la sortie de mon script
a = 12+42
# Je verrai la sortie de mon script
a = 12+42
print(a)

# Exécuter mon script depuis un terminal
# Commande python Chapter1.py
# ou
# chmod u+x Chapter.py
# ./Chapter1.py

# Si j'ai défini des fonctions, les utiliser en interactif :
# - dans un environnement Python :
# import Chapter1
# Chapter1.f(42)
# - dans un script :
# import Chapter1.f as fun1
# fun1(42)

x = 3
y = 1e8
z = 3.14159
print(x, y, z, sep='VM')
print(x, y, z, sep='\n')
print(x,' un truc entre 2', y, sep='--', end='fin\n')

print('''Les hommes de ma vie
Les grands les gros les maigres
J'les aime à la folie
Les p'tits les beaux les bègues''')
print('Mais si je veux couper '
    'une ligne sans passer à la ligne ?')
    
x = 1.23456789
print("Le format g : {:g}".format(x))
print("Le format f : {:.3f}".format(x))
print("Le format f : {:10.3f}".format(x))
print("Le format e : {:.3e}".format(x))
# Aide détaillée : http://docs.python.org/py3k/library/string.html

x = input('Quel chaîne de caractères ? ')
y = eval(input('Quel nombre ? '))

from math import *
print(pi)

# Exécuter une instruction présentée sous forme de chaîne de caractères
var = eval(input('Quelle valeur de variable ? '))
fonc = input('Quelle fonction ? ')
code = ('''def f(x):
   return({}(x))'''.format(fonc))
exec(code)
print('{:5.2f}'.format(f(var)))
    
