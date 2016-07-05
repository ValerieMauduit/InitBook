#!/usr/bin/env python
# -*- coding : Utf-8 -*-

#----- Module TURTTLE ---------------------------------------------------------
from turtle import *
from tkinter import *
from random import *

# Diagramme de Von Koch
def von_karre(l, n): # Tracé d'un segment de longueur l et de profondeur n
    if n == 0:
        forward(l)
    else:
        color(random(), random(), random())
        von_karre(l/3, n-1)
        left(90)
        von_karre(l/3, n-1)
        right(90)
        von_karre(l/3, n-1)
        right(90)
        von_karre(l/3, n-1)
        left(90)
        von_karre(l/3, n-1)
        up()
        backward(2*l/3)
        down()
        color(random(), random(), random())
        von_karre(l/3, n-1)
        up()
        forward(l/3)
        down()

# Tracé d'un flocon de Von Koch
iterations = eval(input('Itérations ? '))
ht()

pen(speed = 0)
up()
goto(-250,0)
down()
von_karre(500,iterations)
#right(180)
#von_karre(500,iterations)

mainloop()
