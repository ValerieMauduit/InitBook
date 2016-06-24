#!/usr/bin/env python
# -*- coding : Utf-8 -*-

from turtle import *
from random import *
from math import *

# Simulation de la machine à clous (bille qui tombe)

def un_tir(n): 
    """ Trouver où tombe la bille pour un tour, 
    avec une pyramide de base n """
    base = list(range(n))
    for etage in range(n-1):
        test = randint(0,1)
        if test == 0:
            base = base[1:]
        else:
            base = base[:-1]
    return base[0]

def un_tir_gr(n, couleur): 
    """ Trouver où tombe la bille pour un tour, 
    avec une pyramide de base n, avec affichage graphique du parcours """
    ht(); pen(speed = 0)
    base = list(range(n))
    color(couleur)
    shape("circle")
    px, py = 0, 250
    up(); goto(px, py); down()
    seth(-90)
    hx, hy = 250 / n, 250 / n
    st(); pen(speed = 1)
    for etage in range(n-1):
        test = randint(0,1)
        if test == 0:
            base = base[1:]
            px, py = px + hx, py - hy
            goto(px, py)
        else:
            base = base[:-1]
            px, py = px - hx, py - hy
            goto(px, py)
    return base[0]
    
def bille(rayon, couleur, posx, posy):
    ht(); pen(speed = 0)
    up(); goto(posx, posy - rayon); seth(0)
    down()
    color(couleur)
    begin_fill(); circle(rayon); end_fill()
    up(); goto(posx - rayon * .4, posy); seth(0)
    down()
    couleur2 = [min(n + .5, 1) for n in couleur]
    color(couleur2)
    begin_fill(); circle(rayon * .3); end_fill()

Lbase = eval(input("Longueur de la base (entier) ? "))
nbe = eval(input("Nombre de billes à faire tomber ? "))
repartition = [0] * Lbase
hx = 250 / Lbase ; 
ht()
pen(speed = 0)
# Faire un graphe où on voit les billes se mettre dans leurs stacks
color(0, 0, 0)
up(); goto(-hx * Lbase, -250); down()
goto(hx * Lbase, -250)
for n in range(Lbase + 1):
    up(); goto(-hx * Lbase + n * hx * 2, - 250); down()
    goto(-hx * Lbase + n * hx * 2, 0); up()

rayon = hx * .8
for indice in range(nbe):
    couleur = (random(), random(), random())
    st(); pen(speed = 1)
    tirage = un_tir_gr(Lbase, couleur)
    repartition[tirage] += 1
    xloc = hx * (-Lbase + 1) + 2 * hx * tirage
    yloc = - 250 + rayon + (repartition[tirage]-1) * 25
    bille(rayon, couleur, xloc, yloc)

#up()
#goto(-hx * Lbase, -250); seth(90)
#down()
#couleur = (random(), random(), random())
#color(couleur)
#for n in range(Lbase):
#    begin_fill()
#    forward(repartition[n] * hy)
#    right(90)
#    forward(2 * hx)
#    left(90)
#    backward(repartition[n] * hy)
#    end_fill()
    
# Conserver l'image
mainloop()

