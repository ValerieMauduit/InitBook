#!/usr/bin/env python
# -*- coding : Utf-8 -*-

# Les structures conditionnelles
#-----------------------------------------------------------------------------

def garcon(nom):
    if nom == 'Christian':
        return('un garçon')
    else:
        return('une fille')
        
toto = input("Qui c'est celui-là ? ")
print("C'est {} !".format(garcon(toto)))

def bissextile(annee):
    if annee%400 == 0:
        return(True)
    elif annee%100 == 0:
        return(False)
    elif annee%4 == 0:
        return(True)
    else:
        return(False)
        
def bissextile2(annee):
    return((annee%400 == 0) or ((annee%4 == 0) and (annee%100 != 0)))
        
A = eval(input('Quelle année testée ? '))
if bissextile(A):
    print("C'est une année bissextile.")
else:
    print("C'est une année normale.")
    
if bissextile2(A):
    print("Test2 : bissextile.")
else:
    print("Test2 : normale.")

# Les boucles while
#-----------------------------------------------------------------------------

def somme(n):
    s = 0
    compteur = 1
    while compteur <= n:
        s = s + compteur ** 2
        compteur += 1
    return(s)
    
N = eval(input('Valeur de n ? '))
print('La somme des {} premiers entiers au '
    'carré est : {}'.format(N,somme(N)))
    
def depasse(M): # Le plus petit n tq somme(n)>M
    n = 1
    while somme(n) <= M:
        n += 1
    return(n)
    
valeur = eval(input("Somme souhaitée ? "))
print("Somme des carrés jusqu'à {} "
    "dépasse {:.0f}".format(depasse(valeur),valeur))

def reste(a,b):
    while a>=b:
        a = a-b 
    return(a)

nb = eval(input("Nombre à diviser ? "))
div = eval(input("Diviseur ? "))
print("Le reste de {:.0f} divisé par {:.0f} est "
    "{:.0f}".format(nb,div,reste(nb,div)))
    
def pgcd(a,b):
    if a<b:
        a, b = b, a
    r = b
    while r != 0:
        r = reste(a,b)
        a, b = b, r
    return(a)
    
nb1 = eval(input("Nombre 1 ? "))
nb2 = eval(input("Nombre 2 ? "))
print("Le PGDC de {:.0f} et {:.0f} est "
    "{:.0f}.".format(nb1,nb2,pgcd(nb1,nb2)))
