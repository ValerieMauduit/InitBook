#!/usr/bin/env python
# -*- coding : Utf-8 -*-

# Compléments sur les fonctions
#------------------------------------------------------------------------------
def f(x, y, z, *args, **keywords, a=1, b=2, c=3):

def composition(f,g):
    return lambda x: f(g(x)) # Définit une fonction standard
    
H = composition(f,g)
H(42)

