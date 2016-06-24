#!/usr/bin/env python
# -*- coding : Utf-8 -*-

from random import *

# Les classes
#-----------------------------------------------------------------------------

class polynome:

    def __init__(self, coefficients):
        self.coefs = coefficients
    def __add__(self, other):
        self.coefs = self.coefs + [0] * (other.deg() - self.deg())
        other.coefs = other.coefs + [0] * (self.deg() - other.deg())
        return polynome([x + y for x, y in zip(self.coefs, other.coefs)])
    def __str__(self):
        affiche = ''
        for i, c in enumerate(self.coefs):
            if i == 0 and c != 0:
                affiche += self.str_monome(i, c)
            elif c < 0:
                affiche += ' ' + self.str_monome(i, c)
            elif c > 0:
                affiche += ' +' + self.str_monome(i, c)
        return affiche
    def __call__(self,x):
        if self.deg() == -1:
            return ''
        elif self.deg() == 0:
            return self.coefs[0]
        else: 
            P = polynome(self.coefs[1:])
            return self.coefs[0] + x * P(x)
        
    def deg(self):
        """Calcul du degré du polynôme"""
        n = len(self.coefs)
        for i, c in enumerate(reversed(self.coefs)):
            if c != 0:
                deg = n - i - 1
                return deg
        return -1
    def str_monome(self, i, c):
        if c == 0:
            return ''
        else:
            if i == 0:
                return str(c)
            elif i == 1:
                return str(c) + '.X'
            else:
                return str(c) + '.X^' + str(i)

l = [randrange(-10, 10) for i in range(4)]
P1 = polynome(l)
print("Le polynome est construit sur {}".format(l))

print("Calcul du degré : {}".format(P1.deg()))

l2 = [randrange(-10, 10) for i in range(3)]
CM = polynome(l2)
print("Le polynome 2 est construit sur {}".format(l2))
AM = P1 + CM
print("p1 + p2 est construit sur {}".format(AM.coefs))

print("Test d'affichage de P1 : {}".format(P1))

val = eval(input('Valeur ? '))
print("Valeur de P1 en {} : {}".format(val,P1(val)))
