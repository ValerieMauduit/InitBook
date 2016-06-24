#!/usr/bin/env python
# -*- coding : Utf-8 -*-

#----- Module TURTTLE ---------------------------------------------------------
from turtle import *
from tkinter import *

# Diagramme de Von Koch
def von_koch(l, n): # Tracé d'un segment de longueur l et de profondeur n
    if n == 0:
        forward(l)
    else:
        von_koch(l/3, n-1)
        left(60)
        von_koch(l/3, n-1)
        right(120)
        von_koch(l/3, n-1)
        left(60)
        von_koch(l/3, n-1)

# Tracé d'un flocon de Von Koch
ht()

iterations = 5
pen(speed = 0)
up()
goto(-250,100)
down()
von_koch(500,iterations)
right(120)
von_koch(500,iterations)
right(120)
von_koch(500,iterations)

mainloop()
