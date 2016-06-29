#!/usr/bin/env python
# -*- coding : Utf-8 -*-

from math import *

#------------------------------------------------------------------------------
# Calcul des points de la courbe d'équation polaire 
# rho = 1 + 1/3 * cos(20 theta/19)

theta = [pi/180 * deg for deg in range(360)]
rho = [1 + 1/3 * cos(20 * t / 19) for t in theta]
polaires = list(zip(theta, rho))

cart = [(r[1] * cos(r[0]), r[1] * sin(r[0])) for r in polaires]

#------------------------------------------------------------------------------
# Ecriture de ces points dans un fichier esclave d'extension .table

fichier = open('courbe.table', 'w')
for l in range(360):
    fichier.write('{:20.10f}{:20.10f}\n'.format(cart[l][0], cart[l][1]))
fichier.close()

#------------------------------------------------------------------------------
# Ecriture d'un fichier maître LaTeX contenant le préambule et 
# l'environnement tikz et appelant le fichier esclave

#------------------------------------------------------------------------------
# Compilation du document maître à l'aide du programme rubber
# https://launchpad.net/rubber


